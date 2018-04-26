# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    topNo = scrapy.Field()  #排名
    name = scrapy.Field()   #电影名
    classify = scrapy.Field()   #分类
    year = scrapy.Field()       #上映年份
    director = scrapy.Field()   #导演
    actors = scrapy.Field()     #演员列表
    score = scrapy.Field()      #豆瓣分数
    
