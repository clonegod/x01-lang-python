# -*- coding: utf-8 -*-

# Scrapy settings for dmoztools project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dmoztools'

SPIDER_MODULES = ['dmoztools.spiders']
NEWSPIDER_MODULE = 'dmoztools.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
   'dmoztools.middlewares.ProxyMiddleware': 100,
}

LOG_FILE = './logs/dmoz_proxy.log'