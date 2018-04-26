# -*- coding: utf-8 -*-
import scrapy
from xiciproxy.items import XiciProxyIpItem

'''从西刺抓取高匿IP，保存到MySQL数据中保存。'''

class XiciproxySpiderSpider(scrapy.Spider):
    name = "xiciproxy"
    allowed_domains = ["xicidaili.comm"]
    start_urls = ['http://www.xicidaili.comm/']
    
    def start_requests(self):
        pageList = []
        for i in range(1,2):
            pageUrl = scrapy.Request("http://www.xicidaili.com/nn/%d" % i)
            pageList.append(pageUrl)
        return pageList
        
    def parse(self, response):
        itemList = []
        for tr in response.css('#ip_list').xpath('.//tr[position() > 1]'):
            item = XiciProxyIpItem()
            item['IP'] = tr.xpath('td[2]/text()').extract_first().strip()
            item['PORT'] = tr.xpath('td[3]/text()').extract_first().strip()
            item['POSITION'] = tr.xpath('string(td[4])').extract_first().strip()
            item['TYPE'] = tr.xpath('td[6]/text()').extract_first().strip()
            item['SPEED'] = tr.xpath('td[7]/div[@class="bar"]/@title').re(r'\d+\.\d+')[0]
            item['LAST_CHECK_TIME'] = tr.xpath('td[10]/text()').extract_first().strip()
            itemList.append(item)
        return itemList