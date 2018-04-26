# -*- coding: utf-8 -*-

# Scrapy settings for xiciproxy project

BOT_NAME = 'xicidaili'

SPIDER_MODULES = ['xiciproxy.spiders']
NEWSPIDER_MODULE = 'xiciproxy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'


# database connection parameters
DBKWARGS={'db':'ippool','user':'root', 'passwd':'root123',
    'host':'192.168.1.201','use_unicode':True, 'charset':'utf8'}


# Configure item pipelines
ITEM_PIPELINES = {
    'xiciproxy.pipelines.XiciCreateDBPipeline': 299,
    'xiciproxy.pipelines.XiciProxyPipeline': 300,
}

