# -*- coding: utf-8 -*-

import scrapy

class QuotesSpider(scrapy.Spider):
    
    # Spider的名称，需保证整个工程内唯一
    name = 'quotes' 
    
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    
    # def start_requests(self):
        # urls = [
            # 'http://quotes.toscrape.com/page/1/',
            # 'http://quotes.toscrape.com/page/2/',
        # ]
        # for url in urls:
            # yield scrapy.Request(url=url, callback=self.parse)
    
    
    # parse() is Scrapy’s default callback method, 
    # which is called for requests without an explicitly assigned callback.
    # 将返回页面保存到本地文件中
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
    