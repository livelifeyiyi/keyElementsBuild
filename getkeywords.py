# -*- coding: utf-8 -*-

import jieba
import jieba.analyse
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

file_dir = 'I:/data/sina_news_article/'

def get_keywords(doc):
	tags = jieba.analyse.extract_tags(doc, topK = 2000)
	keywords = ' '.join(tags)
	file = open(file_dir + '/result/sina_news_keywords.txt','w')
	file.write(keywords)
	file.close()
get_keywords(file_dir + '/combined/sina_news_article.txt')