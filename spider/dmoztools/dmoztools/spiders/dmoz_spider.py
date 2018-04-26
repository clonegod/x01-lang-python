# -*- coding: utf-8 -*-
import scrapy
import codecs

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class DmozSpiderSpider(scrapy.Spider):
    name = "dmoz_spider"
    allowed_domains = ["http://dmoztools.net"]
    
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]
    
    def parse(self, response):
        file = codecs.open(response.url.split('/')[-2] + '.html', 'a+', encoding='utf-8')
        print 'write response to file %s' % file
        file.write(response.body)
        
