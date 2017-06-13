# -*- coding: utf-8 -*-
import re

__author__ = 'Peng'
from bs4 import BeautifulSoup,Comment
import urllib2
from urllib2 import urlopen,HTTPError
import MySQLdb
import json
import datetime
import logging
import sys

#配置日志输出位置为控制台
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                stream=sys.stdout)

#定义一个所有网站的集合。或者每次都查询数据库判读URL是否已存在


def getSinaArticle(url,webname):
    #创建链接集合
    # pages = set()
    #创建字典用来储存函数的返回结果
    dict={'url':url,'title':'','published_time':'','getTime':'','author':'','article':'','webname':webname}

    #创建请求头
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36",
             "Accept":"*/*"}

    #打开网页
    try:
        dict['url']=url
        request = urllib2.Request(url,headers=headers)
        html = urlopen(request)
    except HTTPError as e:
        print(e)
    #读取网页内容并转换成树形文档结构
    soup = BeautifulSoup(html.read(),"lxml")
    conn = getConn();
    cur = conn.cursor()
    for link in soup.findAll("a",href=re.compile(".*?doc-ify.*?")):
    # for link in soup.findAll("a",href=re.compile(r'\d{4}-\d{2}-\d{2}')):
        print link.attrs['href']
        if 'href' in link.attrs:
            sqlQueryUrl="select count(*) from tbl_peng_article where url='%s'"%link.attrs['href']
            result = cur.execute(sqlQueryUrl)
            if ( result < 0 ):
                pass
                # pages.add(link.attrs['href'])

    cur.close()
    conn.close()
    return None

def getConn():
     conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='root',
        db ='nichuiniu',
        charset='utf8',
        )
     return conn

url="http://tech.sina.com.cn/it/2017-06-07/doc-ifyfuzny3756083.shtml"
webname = "sina"

getSinaArticle(url,webname)