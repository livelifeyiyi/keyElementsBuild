# -*- coding: utf-8 -*-
from coolscrapy.items import BaiduBaikeItem
import scrapy
import json
from urlparse import urljoin
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SinaNewsSpider(scrapy.Spider):
	"""get sina envent news"""
	name = "sinaNews"
	llowed_domains = ["sina.com.cn"]
	start_urls = []
	for pagenum in range(1, 100):
		url = "http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=%s&callback=newsloadercallback"%pagenum
		start_urls.append(url)
	def parse(self, response):
		sites = json.loads(response.body_as_unicode())
		item = sinaUrlItem()
		
		data = sites['result']['data']
		for i in range(0, 22):
			item['title'] = data[i]['title']
			item['url'] = data[i]['url']
			item['keywords'] = data[i]['keywords']
		yield item

class SampleSpider(scrapy.Spider):
	# Spider名称，必须是唯一的
	name = "sina"
	allowed_domains = ["sina.com.cn"]
	# start_urls = ["http://tags.news.sina.com.cn/%E6%9A%B4%E6%81%90"] #暴恐标签的新闻
	start_urls = ["http://api.search.sina.com.cn/?q=%E6%9A%B4%E6%81%90&c=news&page=1&num=24&oe=utf-8&range=keyword",
				  "http://api.search.sina.com.cn/?q=%E6%9A%B4%E6%81%90&c=news&page=2&num=24&oe=utf-8&range=keyword",
				  "http://api.search.sina.com.cn/?q=%E6%9A%B4%E6%81%90&c=news&page=3&num=24&oe=utf-8&range=keyword",
				  "http://api.search.sina.com.cn/?q=%E6%9A%B4%E6%81%90&c=news&page=4&num=24&oe=utf-8&range=keyword",
				  "http://api.search.sina.com.cn/?q=%E6%9A%B4%E6%81%90&c=news&page=5&num=24&oe=utf-8&range=keyword"]
	# 用来解析下载后的Response对象
	def parse(self, response):
		# 读取返回的json对象
		sites = json.loads(response.body_as_unicode())
		item = SampleItem()
		for i in range(0, 24):
			url = sites['result']["list"][i]["url"]
			postTime = sites['result']["list"][i]["datetime"]
			keywords = sites['result']["list"][i]["kl"]
			item['postTime'] = postTime
			item['keywords'] = keywords
			yield scrapy.Request(url, meta={'item': item}, callback=self.parse_article)

	def parse_article(self, response):
		# detail = response.xpath('//div[@class="article-wrap"]')
		item = response.meta['item']
		item['title'] = response.xpath('//title/text()')[0].extract()
		
		# item['keywords'] = response.xpath('//meta[@name="keywords"]/text()')[0].extract()
		item['link'] = response.url
		# item['postTime'] = response.xpath('//span[re:test(@class,"time\d$")]/text()')[0].extract()
		body = response.xpath('//div[@id="artibody"]')
		# body = detail.xpath('div[@class="article article_16"]')
		content = ''
		for p in body.xpath('.//p/text()'):
			content += p.extract()
		item['content'] = content
		# item['content'] = detail.xpath('div[@class="article-content-wrap"]/text()')[0].extract()

		print item['title'], item['link'], item['postTime']
		yield item


class BaikeSpider(scrapy.Spider):

	name = "baike"
	# allowed_domains = ["http://baike.baidu.com"]
	# start_urls = ["http://baike.baidu.com/fenlei/%E7%A7%91%E5%AD%A6%E5%AE%B6"]
	start_urls = []
	for i in range(1, 18):
		start_urls.append("http://baike.baidu.com/fenlei/%%E8%%89%%BA%%E6%%9C%%AF%%E5%%AE%%B6?limit=30&index=%s&offset=0#gotoList" % i) #artists
		# scientists
		# http://baike.baidu.com/fenlei/%%E7%%A7%%91%%E5%%AD%%A6%%E5%%AE%%B6?limit=30&index=%s&offset=270#gotoList" % i)

	
	def parse(self, response):
		for sel in response.xpath('//div[@class="g-row p-main"]/div/div[@class="g-row p-entry log-set-param"]/div[@class="grid-list grid-list-spot"]/ul/li'):
			item = BaiduBaikeItem()
			item['name'] = sel.xpath('div[@class="list"]/a/text()')[0].extract()
			# print item['name']
			item['link'] = sel.xpath('div[@class="list"]/a/@href').extract()
			item['summary'] = sel.xpath('div[@class="list"]/p/text()')[0].extract()
			# print item['link']
			url = urljoin("http://baike.baidu.com", str(item['link'][0]))
			
			# url = "http://baike.baidu.com" + str(item['link'])
			# print url
			yield scrapy.Request(url, meta={'item': item}, callback = self.parse_article)
	
	def parse_article(self, response):
		item = response.meta['item']
		item['link'] = response.url
		# body = response.xpath('//div[@class="content-wrapper"]/text()').extract()
		# item['content'] = body
		# tagitems = response.xpath('dd[@id="open-tag-item"]/text()').extract()
		# item['tagitem'] = tagitems

		print item['name'], item['link']
		yield item

