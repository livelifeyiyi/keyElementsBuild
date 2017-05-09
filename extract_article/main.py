#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from cx_extractor import cx_extractor_Python
from sinaNews_url_list import url_list
#import MySQLdb

file_dir = 'K:/data/sina_news_article/'
table_name = 'baike_artists'

def getURLfromDB():
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
i = 831
for url in url_list[832:]:
	i += 1
	print i
	try:
		test_html = cx.getHtml(url)
	except Exception as e:
		print e
		continue
	content = cx.filter_tags(test_html)
	s = cx.getText(content)
	file_name = file_dir + 'sina_news_article' + str(i) + '.txt'
	file = open(file_name, 'w')
	file.write(s)	
	
