# -*- coding: utf-8 -*-

# Importing base64 library because we'll need it ONLY in case 
#if the proxy we are going to use requires authentication
#-*- coding:utf-8-*-
import base64
from proxy import IpPool,counter
import logging
ips=IpPool().get_ips()

class ProxyMiddleware(object):
    http_n=0     #counter for http requests
    https_n=0    #counter for https requests  
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        # 对http请求设置代理
        if request.url.startswith("http://"):
            n=ProxyMiddleware.http_n
            n=n if n<len(ips['http']) else 0 #当所有代理都使用一遍之后，继续循环使用IP列表中的代理IP
            request.meta['proxy']= "http://%s:%d"%(
                ips['http'][n][0],int(ips['http'][n][1]))
            logging.info('HTTP Proxy Squence - http: %s - %s'%(n,str(ips['http'][n])))
            ProxyMiddleware.http_n=n+1
        
        # 对https请求设置代理
        if request.url.startswith("https://"):
            n=ProxyMiddleware.https_n
            n=n if n<len(ips['https']) else 0  #当所有代理都使用一遍之后，继续循环使用IP列表中的代理IP
            request.meta['proxy']= "https://%s:%d"%(
                ips['https'][n][0],int(ips['https'][n][1]))
            logging.info('HTTPS Proxy Squence - https: %s - %s'%(n,str(ips['https'][n])))
            ProxyMiddleware.https_n=n+1 