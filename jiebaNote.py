# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import jieba
import jieba.analyse

#jieba.load_userdict("userDict.txt")
#from data_case import doc
#docPath = 'sina_article.txt'
docPath = './wikidata/wiki.zh.text.jian'
file = open(docPath)
doc = file.read()
#resPath = './jieba_result/sina_default_mode.txt'
resPath = 'jieba_result/wiki.zh.text.jian.seg'
def get_wordseg(doc):
	seg_list = jieba.cut(doc, cut_all=False)
	#print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
	str_default = " ".join(seg_list)
	file = open(resPath,'w')
	file.write(str_default)
	file.close()

 
def get_keywords(doc):
	tags = jieba.analyse.extract_tags(doc, topK = 100)
	keywords = ' '.join(tags)
	file = open('./jieba_result/sina_keywords.txt','w')
	file.write(keywords)
	file.close()
get_wordseg(doc)
#get_keywords(doc)