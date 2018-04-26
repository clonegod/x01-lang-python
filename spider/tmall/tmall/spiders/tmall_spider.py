# -*- coding: utf-8 -*-
import scrapy
from tmall.items import TmallItem

class TmallSpiderSpider(scrapy.Spider):
    name = "tmall_spider"
    
    allowed_domains = ["tmall.com"]
    
    start_urls = ['https://list.tmall.com/search_product.htm?type=pc&totalPage=100&cat=50025135&sort=d&style=g&from=sn_1_cat-qp&active=1&jumpto=10#J_Filter']
    
    
    def parse(self, response):
        divList = response.xpath('//div[@id="J_ItemList"]/div[@class="product  "]/div')
        if not divList:
            self.log( "List Page error--%s" % response.url )
        for div in divList:
            item = TmallItem()
            item['GOODS_NAME'] = div.xpath('p[@class="productTitle"]/a/@title').extract_first()
            item['GOODS_PRICE'] = div.xpath('p[@class="productPrice"]/em/@title').extract_first()
            pre_goods_url = div.xpath('p[@class="productTitle"]/a/@href').extract_first()
            item['GOODS_URL'] = pre_goods_url if "http:" in pre_goods_url else ("http:"+pre_goods_url)
            
            # 图片链接
            try:
                image_urls = div.xpath('div[@class="productImg-wrap"]/a/img/@src|'
                'div[@class="productImg-wrap"]/a[1]/img/@data-ks-lazyload').extract_first()
                item['IMAGE_URLS'] = [ "http:"+image_urls ]
            except Exception,e:
                print "Error: ",e
                import pdb;pdb.set_trace()
            
            yield scrapy.Request(url=item["GOODS_URL"], 
                                 meta={'item':item}, 
                                 callback=self.parse_detail, 
                                 dont_filter=True)
                                 
    def parse_detail(slef, response):
        goodsDetail = response.xpath('//div[@id="detail"]')
        if not goodsDetail:
            self.log( "Detail Page error--%s" % response.url )
        
        item = response.meta['item']
        item['GOODS_SALE'] = goodsDetail.css('.tm-ind-panel').xpath('li[1]/div/span[2]/text()').extract_first()
        item['SHOP_NAME'] = response.xpath('//div[@id="bd"]//h3/div[@class="name"]/a/text()').extract_first()
        item['SHOP_URL'] = response.xpath('//div[@id="bd"]//h3/div[@class="name"]/a/@href').extract_first()
        return item
        