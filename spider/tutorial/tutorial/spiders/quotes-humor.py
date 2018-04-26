# -*- coding: utf-8 -*-

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes-by-tag"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        # 获取命令行参数，如 -a tag=humor 
        tag = getattr(self, 'tag', None)    
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'tag': quote.xpath('//h3/a/text()').extract_first('ALL'),
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)
    