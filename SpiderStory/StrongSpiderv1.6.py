# -*- coding: utf-8 -*-

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
import codecs
import threading
import threading
import Queue
import time
from time import ctime,sleep
# 配置日志信息 输出到控制台
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                stream=sys.stdout)



def getStory(url,webname):
    #创建字典用来储存函数的返回结果
    dict={'url':url,'title':'','published_time':'','getTime':'','author':'','article':'','webname':webname}

    #执行结果
    rs = 0

    #创建请求头
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36",
             "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
             "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
             "Referer":"https://www.baidu.com/s?ie=UTF-8&wd=sina"}

    #打开网页
    try:
        dict['url']=url
        request = urllib2.Request(url,headers=headers)
        html = urlopen(request)
    except Exception as e:
        print(e)

    #解析内容时如果有异常就捕获并返回空
    try:
        #读取网页内容并转换成树形文档结构
        soup = BeautifulSoup(html.read(),"lxml")

        f1 = codecs.open('C:\\Users\\Peng\\Desktop\\zzzz.txt','a','utf-8')
        paragraph = soup.find(id=re.compile("postmessage_\d+"));
        f1.write('\r\nBEGIN-----------------------------------------------------\r\n')
        f1.write(paragraph.get_text())
        f1.write('\r\nEND+++++++++++++++++++++++++++++++++++++++++++++++++++++\r\n')
        f1.close()
        rs = 1
    except:
        return None
    return rs


def GO(url,webname,i):

    #创建请求头
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36",
             "Accept":"*/*"}

    #打开网页
    try:
        request = urllib2.Request(url,headers=headers)
        html = urlopen(request)
    except Exception as e:
        print(e)
    #读取网页内容并转换成树形文档结构
    soup = BeautifulSoup(html.read(),"lxml")
    #声明一个数组用来存储入库的文章链接
    L = []

    #获取form的个数，然后取最后一个,一般有两个以上的form，只需要最后一个form的url
    form = soup.find_all(summary=re.compile("forum_\d+"))
    length = len(form)
    lastFrom = form[length-1]

    #获取最后一个form下的所有url
    for link in lastFrom.findAll("a",href=re.compile(r'(.*?)(thread)(-)(\d+)(-1-)'+str(i)+'(.html)')):
        if 'href' in link.attrs:
            #提取href中的url，并规范格式去除分页参数
            xurl = link.attrs['href']
            L.append(xurl)

    #去除重复的列元素
    L2 = list(set(L))
    #获取所有拼装好的url
    urls = []
    for item in L2:
        fullurl = "http://xxxxx.com/bbs/"+item
        urls.append(fullurl)
    return  urls

class worker(threading.Thread):
    def __init__(self,url, name):
        threading.Thread.__init__(self)
        self.url = url
        self.name = name
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            print("thread%d %s: waiting for task" %(self.ident,self.name))
            getStory(self.url,'xxx')
            self.thread_stop = True

    def stop(self):
        self.thread_stop = True


def createThread(urls,Tnum):
    threadList = []
    for i in range(0,Tnum):
        threadList.append(str(i))

    threads = []
    # 创建新线程
    m=0
    for tName in threadList:
        try:
            thread = worker(urls[m], tName)
            thread.start()
            threads.append(thread)
            m += 1
        except Exception as e:
            print e
    # 等待所有线程完成
    # join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。
    #join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
    for t in threads:
        t.join()
    # sleep(0.5)


logging.info("begin spider  ")
webname="xyz"
for i in range (1,66):
    url="http://xxxxx.com/xxx-"+str(i)+".html"
    #获取所有拼装好的url
    urls = GO(url,webname,i)
    createThread(urls,len(urls))
    # for url in urls:
    #     createThread(url)
    #     print url



logging.info("end spider  ")

#多线程

