# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from coolscrapy.items import SampleItem
import scrapy
import json

class SampleSpider(scrapy.Spider):
	#Spider名称，必须是唯一的
	name = "sina"
	allowed_domains = ["sina.com.cn"]
	#start_urls = ["http://tags.news.sina.com.cn/%E6%9A%B4%E6%81%90"] #暴恐标签的新闻
	start_urls = ["http://api.search.sina.com.cn/?q=%E6%9A%B4%E6%81%90&c=news&page=1&num=24&oe=utf-8&range=keyword",
				  "http://api.search.sina.com.cn/?q=%E6%9A%B4%E6%81%90&c=news&page=2&num=24&oe=utf-8&range=keyword",
				  "http://api.search.sina.com.cn/?q=%E6%9A%B4%E6%81%90&c=news&page=3&num=24&oe=utf-8&range=keyword",
				  "http://api.search.sina.com.cn/?q=%E6%9A%B4%E6%81%90&c=news&page=4&num=24&oe=utf-8&range=keyword",
				  "http://api.search.sina.com.cn/?q=%E6%9A%B4%E6%81%90&c=news&page=5&num=24&oe=utf-8&range=keyword"]
	#用来解析下载后的Response对象
	def parse(self, response):
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
		#detail = response.xpath('//div[@class="article-wrap"]')
		item = response.meta['item']
		item['title'] = response.xpath('//title/text()')[0].extract()
		
		#item['keywords'] = response.xpath('//meta[@name="keywords"]/text()')[0].extract()
		item['link'] = response.url
		#item['postTime'] = response.xpath('//span[re:test(@class,"time\d$")]/text()')[0].extract()
		body = response.xpath('//div[@id="artibody"]')
		#body = detail.xpath('div[@class="article article_16"]')
		content = ''
		for p in body.xpath('.//p/text()'):
			content += p.extract()
		item['content'] = content
		#item['content'] = detail.xpath('div[@class="article-content-wrap"]/text()')[0].extract()

		print item['title'], item['link'], item['postTime']
		yield item
