# -*- coding: utf-8 -*-

import sys
from dbutil import exec_sql
import socket
import urllib2

dbapi="MySQLdb"
kwargs={'user':'root','passwd':'root123','db':'ippool','host':'192.168.1.201', 'use_unicode':True}

def counter(start_at=0):
    '''Function: count number
    Usage: f=counter(i) print f() #i+1'''
    count=[start_at]
    # closure 保护内部变量不被外界直接修改
    def incr():
        count[0]+=1
        return count[0]
    return incr

def use_proxy (browser,proxy,url):
    '''Open browser with proxy'''
    #After visited transfer ip
    profile=browser.profile
    profile.set_preference('network.proxy.type', 1)  
    profile.set_preference('network.proxy.http', proxy[0])  
    profile.set_preference('network.proxy.http_port', int(proxy[1]))  
    profile.set_preference('permissions.default.image',2)
    profile.update_preferences() 
    browser.profile=profile
    browser.get(url)
    browser.implicitly_wait(30)
    return browser
    
class Singleton(object):
    '''Signal instance example.'''
    def __new__(cls, *args, **kw):  
        if not hasattr(cls, '_instance'):  
            orig = super(Singleton, cls)  
            cls._instance = orig.__new__(cls, *args, **kw)  
        return cls._instance 

class IpPool(Singleton):
    
    # 从数据库查询一批代理IP
    def __init__(self):
        sql='''SELECT  `IP`,`PORT`,`TYPE`
        FROM  `proxy` 
        WHERE `TYPE` REGEXP  'HTTP|HTTPS'
        AND  `SPEED`<5 OR `SPEED` IS NULL
        ORDER BY `proxy`.`TYPE` ASC 
        LIMIT 50 '''
        self.result = exec_sql(sql,**kwargs)
        
    # 删除失效代理IP
    def del_ip(self,record):
        '''delete ip that can not use'''
        sql="delete from proxy where IP='%s' and PORT='%s'"%(record[0],record[1])
        print "--->%s" % sql
        exec_sql(sql,**kwargs)
        print record ," was deleted."
    
    # 测试代理IP的可用性
    def check_usable(self,record):
        '''Judge IP can use or not'''
        http_url="http://dmoztools.net/"
        https_url="https://www.alipay.com/"
        proxy_type=record[2].lower()
        url=http_url if  proxy_type== "http" else https_url
        proxy="%s:%s"%(record[0],record[1])
        try:
            req=urllib2.Request(url=url)
            req.set_proxy(proxy,proxy_type)
            response=urllib2.urlopen(req,timeout=10)
        except Exception,e:
            print "Request Error:",e
            self.del_ip(record)
            return False
        else:
            code=response.getcode()
            if code>=200 and code<400:
                print 'Effective proxy',record
                return True
            else:
                print 'Invalide proxy',record
                self.del_ip(record)
                return False
    
    # 获取一批可用的代理IP
    def get_ips(self):
        print "Proxy getip was executed."
        httpList = [record[0:2] for record in self.result if record[2] =="HTTP" and self.check_usable(record)]
        httpsList = [record[0:2] for record in self.result if record[2] =="HTTPS" and self.check_usable(record)]
        print "Http: ",len(httpList),"Https: ", len(httpsList)
        return {"http":httpList, "https":httpsList}