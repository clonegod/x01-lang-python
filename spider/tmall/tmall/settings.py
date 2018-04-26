# -*- coding: utf-8 -*-

# Scrapy settings for tmall project

BOT_NAME = 'tmall'

SPIDER_MODULES = ['tmall.spiders']
NEWSPIDER_MODULE = 'tmall.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Enable or disable downloader middlewares
# DOWNLOADER_MIDDLEWARES = {
   # 'tmall.middlewares.JavaScriptDownloaderMiddleware': 543,
   # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None
# }


# Configure item pipelines
ITEM_PIPELINES = {
    #根据ITEM中存储的图片链接自动下载图片
    'scrapy.pipelines.images.ImagesPipeline': 1,
    # 'tmall.pipelines.TmallPipeline': 300,
}

# 指定图片链接从ITEM的哪个字段获取
IMAGES_URLS_FIELD = 'IMAGE_URLS'
# 指定图片存储路径（图片名称为图片URL的SHA1哈希值）
IMAGES_STORE = r'./images/'

