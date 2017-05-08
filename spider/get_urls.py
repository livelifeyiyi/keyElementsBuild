import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
class SinaNewsSpider(scrapy.Spider):
	#get sina envent news
	name = "sinaNews"
	llowed_domains = ["sina.com.cn"]
	start_urls = []
	for pagenum in range(1, 100):
		url = "http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=%s&callback=newsloadercallback"%pagenum
		start_urls.append(url)
"""

start_urls = []
for pagenum in range(1, 100):
	url = "http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=%s&callback=newsloadercallback"%pagenum
	start_urls.append(url)
		
def http_get(url):
	response = urllib2.urlopen(url)
	return response.read()
url_list = []
for url in start_urls:
	#item = {'title':'', 'url':'', 'keywords':''}
	ret = http_get(url)
	ret_json = ret[21:-2]
	sites = json.loads(ret_json)
	data = sites['result']['data']
	for i in range(0, 22):
		url_list.append(data[i]['url'])
file = open('sinaNews_url_list.txt', 'w+')
#line = url_list.encode("utf-8")
file.write(str(url_list))