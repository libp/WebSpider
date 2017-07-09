# -*- coding: utf-8 -*- 
__author__ = 'Peng'
from bs4 import BeautifulSoup,Comment
import urllib2
from urllib2 import urlopen,HTTPError
import MySQLdb
import json
import datetime
import logging
import sys
import re
import time
import random

def getSinaArticle(url):
    #创建请求头
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36",
             "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
             "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
             "Referer":"https://www.baidu.com/s?ie=UTF-8&wd=sina"}

    #打开网页
    try:

        request = urllib2.Request(url,headers=headers)
        html = urlopen(request)
        soup = BeautifulSoup(html.read(),"lxml")
        print soup.prettify()
    except HTTPError as e:
        print(e)

url="http://news.sina.com.cn/"
getSinaArticle(url)