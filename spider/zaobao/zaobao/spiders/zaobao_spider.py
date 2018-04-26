# -*- coding: utf-8 -*-
import scrapy


class ZaobaoSpiderSpider(scrapy.Spider):
    name = "zaobao"
    allowed_domains = "zaobao.com"
    
    start_urls=["http://www.zaobao.com/special/report/politic/fincrisis"]

    def parse(self, response):
        for href in response.css('.post-list').xpath('./div/div/a/@href'):
            full_url = response.urljoin(href.extract())
            print full_url
            yield scrapy.Request(full_url, callback=self.parse_news)

    def parse_news(self, response):
        yield {
            'title':response.css('#MainCourse h1::text').extract_first(),
            'date':response.css("aside .datestamp::text").extract_first(),
            'body':response.css("#FineDining").extract_first(),
            'link': response.url,
        }
