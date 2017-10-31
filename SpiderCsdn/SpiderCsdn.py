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
import ConfigParser

import smtplib
from email.mime.text import MIMEText
from email.header import Header
reload(sys)
sys.setdefaultencoding('utf8')
# 配置日志信息 输出到控制台
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                stream=sys.stdout)


def SendEmail(mail_msg):
    config = ConfigParser.ConfigParser()
    config.readfp(open("config.ini"), "r")
    strFrom = config.get("email", "sender")
    strTo = config.get("email", "receivers")

    message = MIMEText(mail_msg, 'html', 'utf-8')
    subject = 'CSDN 数据监控'
    message['Subject'] = Header(subject, 'utf-8')
    message['To'] = strTo;
    message['From'] = strFrom;
    smtp = smtplib.SMTP('smtp.qq.com')
    smtp.login(config.get("email", "sender"),config.get("email", "passwd"))
    try:
        smtp.sendmail(strFrom,strTo,message.as_string())
    finally:
        smtp.close



def getContent(url,webname):
    #创建字典用来储存函数的返回结果
    dict={'access':'','score':'','level':'','ranking':'','getTime':''}

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
    except HTTPError as e:
        print(e)

    #解析内容时如果有异常就捕获并返回空
    try:
        #读取网页内容并转换成树形文档结构
        soup = BeautifulSoup(html.read(),"lxml")

        #去除html注释
        for element in soup(text=lambda text: isinstance(text, Comment)):
            element.extract()

        #过滤JavaScript
        [s.extract() for s in soup('script')]

        #获取blog_rank
        # dict['access'] = soup.find(id="blog_rank").find_all('li')[0].span.get_text()
        # dict['score'] = soup.find(id="blog_rank").find_all('li')[1].span.get_text()
        # dict['ranking'] = soup.find(id="blog_rank").find_all('li')[3].span.get_text()
        #不如直接传html过去好了
        dict['access'] = soup.find(id="blog_rank").find_all('li')[0]
        dict['score'] = soup.find(id="blog_rank").find_all('li')[1]
        dict['ranking'] = soup.find(id="blog_rank").find_all('li')[3]

        # print dict['access']
        # print dict['score']
        # print dict['ranking']

    except:
        return None
    return dict





logging.info("begin spider csdn news")
url="http://blog.csdn.net/u011350541?viewmode=contents"
webname="csdn"
dict =  getContent(url,webname)
mail_msg = """
<ul type='circle'>
%s
%s
%s
<li>%s</li>
</ul>
"""%(dict['access'],dict['score'],dict['ranking'],str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
SendEmail(mail_msg)
logging.info("end spider csdn tech")

#这个爬虫我想做一些改变，遍历整个新浪news！！