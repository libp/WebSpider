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

def getInfinity(i):

    #创建请求头
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36",
             "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
             "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
             "Referer":"https://www.baidu.com/s?ie=UTF-8&wd=sina"}

    try:
        url="https://img.infinitynewtab.com/wallpaper/"+str(i)+".jpg"
        request = urllib2.Request(url,headers=headers)
        html = urlopen(request)
        data = html.read()
        imgName = str(i)+".jpg"
        f = open("D:\\infinity2\\"+imgName, 'wb')
        f.write(data)
        print u"正在保存的图片为",imgName
        f.close()
    except HTTPError as e:
        print(e)




class worker(threading.Thread):
    def __init__(self,id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            print("thread%d %s: waiting for task" %(self.ident,self.name))
            getInfinity(self.id)
            self.thread_stop = True

    def stop(self):
        self.thread_stop = True


def createThread(id,Tnum):
    threadList = []
    for i in range(1,Tnum):
        threadList.append(str(i))

    threads = []
    # 创建新线程
    for tName in threadList:
        thread = worker(id, tName)
        thread.start()
        threads.append(thread)
        id += 1
    # 等待所有线程完成
    # join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。
    #join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
    for t in threads:
        t.join()
    # sleep(0.5)

def startDownload(l,Tnum):
    for i in range(1,l,Tnum):
        createThread(i,Tnum)

startDownload(4050,100)

#01
#这并不是我想要的多线程高并发，目前只是一次起了100个进程，但是起完100个进程之后，还是要等待大约3到5秒，
#再发起下一次请求，我想要的是它一直在发请求，一直不断的在读写下载。

#02
#在01思考的基础上，我注释掉join()方法就实现了我的目标

#03
#02似乎存在连接丢失的情况，有join时能够保证下载所有的目标图片，没有join大概有1/4的连接丢失
#所以还是加上join，等1批线程执行完再走第二批比较好