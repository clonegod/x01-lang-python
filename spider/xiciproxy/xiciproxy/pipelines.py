# -*- coding: utf-8 -*-

import sys
import MySQLdb


# 用于初始化MySQL数据库及表的PipeLine。
class XiciCreateDBPipeline(object):
    init = False
    def process_item(self, item, spider):
        if self.init == False:
            DBKWARGS = spider.settings.get('DBKWARGS')
            # 如果数据库还不存在，则需要删除数据库连接参数中的db键。因为此时数据库还不存在！
            # 创建一个DBKWARGS的副本
            DBKWARGS_COPY = DBKWARGS.copy()
            DBKWARGS_COPY.pop('db')
            print '------------>>>db not exist, init database: %s' % DBKWARGS_COPY
            conn = MySQLdb.connect(**DBKWARGS_COPY)
            cursor = conn.cursor()
            try:
                cursor.execute('''CREATE DATABASE IF NOT EXISTS ippool;''')
                conn.select_db('ippool');
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS `proxy` (
                      `IP` varchar(255) NOT NULL DEFAULT '',
                      `PORT` varchar(255) NOT NULL DEFAULT '',
                      `TYPE` varchar(255) DEFAULT NULL,
                      `GET_POST` varchar(255) DEFAULT NULL,
                      `POSITION` varchar(255) DEFAULT NULL,
                      `SPEED` varchar(255) DEFAULT NULL,
                      `LAST_CHECK_TIME` varchar(255) DEFAULT NULL,
                      PRIMARY KEY (`IP`,`PORT`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
                    ''')
                conn.commit()
                self.init = True
            except Exception,e:
                print "Insert error:",e
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
        else:
            print '------------>>>db exist, do nothing.'
        return item

        
        
# 保存抓取数据到MySQL的PipeLine
class XiciProxyPipeline(object):
    def process_item(self, item, spider):
        # 从settings中读取连接数据库的参数
        DBKWARGS = spider.settings.get('DBKWARGS')
        conn = MySQLdb.connect(**DBKWARGS)
        cursor = conn.cursor()
        sql = ("insert into proxy(IP,PORT,TYPE,POSITION,SPEED,LAST_CHECK_TIME) "
               "values (%s,%s,%s,%s,%s,%s)")
        values = (item['IP'],item['PORT'],item['TYPE'],item['POSITION'],item['SPEED'],item['LAST_CHECK_TIME'])
        try:
            print sql
            print values
            cursor.execute(sql, values)
        except Exception,e:
            print "Insert error:",e
            conn.rollback()
        else:
            conn.commit()
        cursor.close()
        conn.close()
        
        return item
