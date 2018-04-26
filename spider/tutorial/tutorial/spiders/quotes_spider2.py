# -*- coding: utf-8 -*-

import scrapy

class QuotesSpider(scrapy.Spider):
    
    # Spider的名称，需保证整个工程内唯一
    name = 'quotes2' 
    
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    
    # parse() is Scrapy’s default callback method, 
    # which is called for requests without an explicitly assigned callback.
    # 解析返回页面，提取内容并封装到dict中,返回dict
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
    