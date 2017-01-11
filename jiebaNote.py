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
	#doc = "我来到北京清华大学"
	''''seg_list = jieba.cut(doc, cut_all=True)
	#print("Full Mode: " + "/ ".join(seg_list))  # 全模式
	str_full = "/ ".join(seg_list)
	file = open('./jieba_result/full_mode.txt','w')
	file.write(str_full)
	file.close()'''

	seg_list = jieba.cut(doc, cut_all=False)
	#print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
	str_default = " ".join(seg_list)
	file = open(resPath,'w')
	file.write(str_default)
	file.close()

	'''
	#新词发现e.g.
	str1 = '你看过穆赫兰道吗'
	#ztr1 ="他来到了网易杭研大厦"
	seg_list = jieba.cut(doc)  # 默认是精确模式
	print(", ".join(seg_list))'''

	'''
	#"小明硕士毕业于中国科学院计算所，后在日本京都大学深造"
	seg_list = jieba.cut_for_search(doc)  # 搜索引擎模式
	#print(", ".join(seg_list))
	str_search = "/ ".join(seg_list)
	file = open('./jieba_result/search_mode.txt','w')
	file.write(str_search)
	file.close()'''

def get_keywords(doc):
	tags = jieba.analyse.extract_tags(doc, topK = 100)
	keywords = ' '.join(tags)
	file = open('./jieba_result/sina_keywords.txt','w')
	file.write(keywords)
	file.close()
get_wordseg(doc)
#get_keywords(doc)