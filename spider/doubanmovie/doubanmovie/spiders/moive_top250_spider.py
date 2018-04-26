#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from doubanmovie.items import DoubanMovieItem

class MoiveTop250SpiderSpider(scrapy.Spider):
    
    name = "doubanMovieTop250"
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        for movie_info in response.css('.item').css('a::attr(href)').extract():
            self.logger.info('request movie_info:%s' % movie_info)
            yield scrapy.Request(movie_info, self.parse_movie)
        
        next_page = response.css('.paginator').css('.next').css('a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            self.logger.info('request next_page:%s' % next_page)
            yield scrapy.Request(next_page, self.parse)
    
    def parse_movie(slef, response):
        item = DoubanMovieItem()
        sel = Selector(response)
        item['topNo'] = sel.css('.top250-no::text').extract()
        item['name'] = sel.xpath('//div[@id="content"]/h1/span[1]/text()').extract()
        item['year'] = sel.xpath('//div[@id="content"]/h1/span[2]/text()').re(r'(\d+)')
        item['classify'] = sel.xpath('//div[@id="info"]//span[@property="v:genre"]/text()').extract()
        item['director'] = sel.xpath('//div[@id="info"]/span[1]//a/text()').extract()
        item['actors'] = sel.xpath('//div[@id="info"]//span[@class="actor"]//a/text()').extract()
        item['score'] = sel.xpath('//div[@id="interest_sectl"]//strong[@property="v:average"]/text()').extract()
        return item