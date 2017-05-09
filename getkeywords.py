# -*- coding: utf-8 -*-

import jieba
import jieba.analyse
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

file_dir = 'D:/data/sina_news_article/'

def get_keywords(doc):

	tags = jieba.analyse.extract_tags(doc, withWeight=True, topK = 20)
	print tags
	print type(tags)
	keywords = ' '.join(str(tags))
	file = open(file_dir + '/combined/sina_news_keywords2.txt','w')
	file.write(keywords)
	file.close()
#docPath = file_dir + '/combined/sina_news_article.txt'
docPath = file_dir + 'sina_news_article1.txt'
file = open(docPath)
doc = file.read()
get_keywords(doc)
#get_keywords(file_dir + 'sina_news_article1.txt')