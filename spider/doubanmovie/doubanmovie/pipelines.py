# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

class DoubanMoviePipeline(object):

    def __init__(self):
        # 用UTF-8编码保存中文字符
        self.file = codecs.open('./data/douban_movie_top250_utf8.json', 'w', encoding='utf-8')
    
    def process_item(self, item, spider):
        # 不使用ASCII编码保存数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    
    def spider_closed(self, spider):
        self.file.close()
