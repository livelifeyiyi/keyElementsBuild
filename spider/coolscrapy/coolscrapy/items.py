# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BaiduBaikeItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    summary = Field()
    #category = Field()
    link = Field()
    #postTime = Field()
    #content = Field()
    #tagitem = Field()
class SampleItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    summary = Field()
    #category = Field()
    link = Field()
    postTime = Field()
    content = Field()
    keywords = Field()
class sinaUrlItem(Item):
    title = Field()
    url = Field()
    keywords = Field()