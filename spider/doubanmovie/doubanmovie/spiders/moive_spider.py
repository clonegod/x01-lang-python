# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from doubanmovie.items import DoubanMovieItem

class MoiveSpiderSpider(CrawlSpider):
    name = 'doubanMovie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        # 电影列表页的URL规则
        Rule(LinkExtractor(allow=(r'\?start=\d+&filter='))),
        # 电影详情页的URL规则
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/subject/\d+/')), callback='parse_item'),
    )

    def parse_item(self, response):
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
