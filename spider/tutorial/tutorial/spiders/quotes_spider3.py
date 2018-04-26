# -*- coding: utf-8 -*-

import scrapy

class QuotesSpider(scrapy.Spider):
    
    # Spider的名称，需保证整个工程内唯一
    name = 'quotes3' 
    
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]
    
    # parse() is Scrapy’s default callback method, 
    # which is called for requests without an explicitly assigned callback.
    def parse(self, response):
        # 解析返回页面，提取内容并封装到dict中,返回dict
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
        
        # 接着请求下一页
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            print '------------before urljoin, next_page: %s' % next_page
            next_page = response.urljoin(next_page)
            print '------------after urljoin, next_page: %s' % next_page
            yield scrapy.Request(next_page, callback=self.parse)
    