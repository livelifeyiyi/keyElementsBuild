#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from cx_extractor import cx_extractor_Python

import MySQLdb

file_dir = 'I:/data/baidubaike_person_article/artists/'
table_name = 'baike_artists'

db = MySQLdb.connect("127.0.0.1","root","root","spider",charset='utf8' )
cursor = db.cursor()

cursor.execute("""SELECT url, name FROM %s
	""" % table_name)
rows = cursor.fetchall()
url_list, name = [], []
for row in rows:
	print row
	url_list.append(row[0])
	name.append(row[1].decode('utf-8'))
print row
cx = cx_extractor_Python()
# test_html = cx.readHtml("E:\\Documents\\123.html") #html代码文件
#url = "http://news.sina.com.cn/c/nd/2017-01-08/doc-ifxzkfuh6130021.shtml"
i = 0
for url in url_list:
	test_html = cx.getHtml(url)
	content = cx.filter_tags(test_html)
	s = cx.getText(content)
	file_name = file_dir + name[i] + '.txt'
	file = open(file_name, 'w')
	file.write(s)
	print i
	i += 1
