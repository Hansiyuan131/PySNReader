# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['news.baidu.com']
    start_urls = ['http://news.baidu.com/']

    def parse(self, response):
        pass
