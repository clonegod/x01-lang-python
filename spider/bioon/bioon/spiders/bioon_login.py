# -*- coding: utf-8 -*-
import scrapy
import json

# 通过环境变量为Request设置全局代理
import os
os.environ['http_proxy'] = 'http://127.0.0.1:8888'

class BioonLoginSpider(scrapy.Spider):
    name = "bioon_login"
    allowed_domains = ["bioon.com"]
    start_urls = ['http://login.bioon.com/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formid='login_form',
            formdata={'account':'asynclife@163.com', 
                      'username': 'asynclife@163.com', 
                      'password': '123456', 
                      'login-btn':'0', 
                      'grant_type':'password'},
            clickdata = {'id':'login-btn'},
            callback=self.after_login
        )
    
    def after_login(self, response):
        print response.body
        # 将json字符串转为dict
        res = json.loads(response.body)
        # check login succeed before going on
        if res['status']==0:
            self.logger.info("Login success")
            # 注销登录
            return scrapy.Request(url='http://news.bioon.com/user/outLog.do', callback=self.logout)
        else:
            self.logger.error("Login failed")
    
    def logout(self, response):
        print 'logout success'
        return