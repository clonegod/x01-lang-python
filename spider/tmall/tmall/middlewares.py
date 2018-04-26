# -*- coding: utf-8 -*-


from scrapy import signals


from selenium import webdriver
from scrapy.http import HtmlResponse
import time

class JavaScriptDownloaderMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == "tmall_spider":
            print "PhantomJS is starting..."
            #指定使用的浏览器
            driver = webdriver.PhantomJS()
            #driver = webdriver.Firefox()
            driver.get(request.url)
            time.sleep(3)
            # js = "var q=document.documentElement.scrollTop=10000" 
            #可执行js，模仿用户操作。此处为将页面拉至最底端。
            # driver.execute_script(js) 
            # time.sleep(3)
            body = driver.page_source
            print (u"访问"+request.url)
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return