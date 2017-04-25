# -*- coding: utf-8 -*-
import os
import jieba
import jieba.analyse
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import MySQLdb
db = MySQLdb.connect("127.0.0.1","root","root","spider",charset='utf8' )
cursor = db.cursor()

import time
nowtime = time.strftime('%Y-%m-%d %H:%M:%S')
path = 'I:/data/baidubaike_person_article/artists/'

class personArticleHandler(object):
	"""To process the articles to extract the top 100 tags from baiduBaike person descriptions."""
	def getTags(self, path):
		#self.arg = arg
		i = 1
		if os.path.isdir(path):
			for fpath,path,fnames in os.walk(path):
				for fname in fnames:
					fname_path = os.path.join(fpath,fname)
					person_name = fname.split('.')[0]
					fo = open(fname_path, 'r')
					person_descrb = fo.read()
					tags = jieba.analyse.extract_tags(person_descrb, topK = 100)
					#print person_name
					#print tags
					#print path,type(path)
					file_name = 'I:/data/baidubaike_person_article/jieba_tag/' + str(person_name) + '.txt'
					file = open(file_name, 'w')
					file.write(", ".join(tags))
					#cursor.execute("""INSERT into artists_tags (name, tags) VALUES (%s, %s) """%(person_name, str(tags)))
					print i
					i += 1
	def test(self):
		listvalue = [u'Alejandro', u'\u4e13\u8f91', u'Sanz', u'\u5929\u6d25\u5e02', u'....', u'\u5165\u9009', u'\u4e66\u753b', u'\u9970\u6f14', u'\u62c9\u4e01', u'No', u'\u5408\u4f5c\u8005', u'La', u'Lo', u'De', u'Es', u'\u4f5c\u54c1\u5c55\u89c8', u'\u897f\u73ed\u7259', u'1993', u'Me', u'\u6b4c\u66f2', u'\u4e66\u753b\u5c55', u'\u6cb3\u5317\u6886\u5b50', u'10', u'\u6b4c\u795e', u'Si', u'\u7814\u7a76\u4f1a', u'\u4e13\u8f91\u540d\u79f0', u'\u4e2d\u56fd', u'1996', u'Mismo', u'El', u'Que', u'Los', u'\u827a\u672f', u'\u4e16\u754c\u534e\u4eba', u'\u7f8e\u672f', u'\u97f3\u4e50', u'\u5468\u5e74', u'\u6cb3\u5317\u7701', u'\u56fd\u9645', u'Mi', u'\u4e3e\u529e', u'\u4e66\u753b\u4f5c\u54c1', u'\u8001\u5e74', u'\u6700\u4f73', u'\u6b4c\u624b', u'1995', u'11', u'Se', u'Te', u'\u845b\u83b1\u7f8e\u5956', u'Al', u'2000', u'\u66f2\u76ee', u'\u5907\u6ce8', u'\u5929\u6d25', u'\u4f5c\u54c1', u'\u4e66\u6cd5', u'\u4f18\u79c0\u5956', u'\u5927\u8d5b', u'\u5f53\u4ee3', u'\u55d3\u97f3', u'\u6d41\u884c', u'\u653f\u534f', u'\u5355\u66f2', u'\u8363\u8a89\u5956', u'Primera', u'Part', u'2001', u'Yo', u'Coraz', u'\u5355\u66f2\u699c', u'1983', u'\u5c55\u89c8', u'\u8bc4\u5206', u'\u6587\u5316', u'\u827a\u672f\u8282', u'\u56fd\u753b\u5bb6', u'\u4e66\u753b\u9662', u'\u5409\u4ed6', u'\u91d1\u5956', u'\u5267\u56e2', u'\u6f14\u5458', u'\u4e66\u753b\u827a\u672f', u'\u4e16\u754c', u'\u53d1\u884c', u'1997', u'50', u'He', u'Miras', u'Son', u'2006', u'2007', u'2004', u'lo', u'Flamenco', u'\u4f18\u79c0', u'\u6f14\u51fa', u'\u4e2d\u56fd\u4e66\u753b', u'\u4f1a\u5458']
		print ", ".join(listvalue)
handler = personArticleHandler()
handler.getTags(path)
#handler.test()