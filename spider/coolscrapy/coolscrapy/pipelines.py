# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime

import logging
from contextlib import contextmanager

from scrapy import signals
from scrapy.exporters import JsonItemExporter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker
from coolscrapy.models import db_connect, create_news_table, Article
import json

class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('items.txt', 'w+')
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item

class TxtWriterPipeline(object):
    '''将正文内容写入1个文本'''
    def __init__(self):
        self.file = open('sina_article.txt', 'w+')
    def process_item(self, item, spider):
        line = item['content'].encode("utf-8")
        self.file.write(line)
        return item


class ArticleDataBasePipeline(object):
    """保存文章到数据库"""

    def __init__(self):
        engine = db_connect()
        create_news_table(engine)
        #create session, use session to handle the database
        self.Session = sessionmaker(bind=engine)

    def open_spider(self, spider):
        """This method is called when the spider is opened."""
        pass

    @contextmanager
    def session_scope(self, session):
        """Provide a transactional scope around a series of operations."""
        #session = Session()  #note the "()" here
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def process_item(self, item, spider):
        a = Article(url=item["link"],
                    title=item["title"].encode("utf-8"),
                    publish_time=item["postTime"].encode("utf-8"),
                    body=item["content"].encode("utf-8"),
                    keywords=item['keywords'].encode("utf-8"),
                    )
        # summary=item['summary'].encode("utf-8"),
        # source_site=item["source_site"].encode("utf-8")
        with self.session_scope(self.Session()) as session:
            session.add(a)
        return item

    def close_spider(self, spider):
        pass


'''
class CoolscrapyPipeline(object):
    def process_item(self, item, spider):
        return item
'''
