# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmallItem(scrapy.Item):
    GOODS_NAME = scrapy.Field()     #商品名称
    GOODS_PRICE = scrapy.Field()    #商品价格
    GOODS_URL = scrapy.Field()      #商品详情页连接
    GOODS_SALE = scrapy.Field()     #商品销量
    SHOP_NAME = scrapy.Field()      #店铺名称
    SHOP_URL = scrapy.Field()       #店铺链接
    IMAGE_URLS = scrapy.Field()     #商品图片链接
