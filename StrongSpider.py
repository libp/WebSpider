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

#配置日志输出位置为控制台
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                stream=sys.stdout)


def spiderSinaTech(url,webname):
     conn = getConn();
     cur = conn.cursor()

     data = getSinaArticle(url,webname)
     if (data == None):
         #不能解析目标网页
         return -1
     try:
         sqlInsertArticle="insert into tbl_peng_article (title,author,content,createTime,getTime,url,webname) values (%s,%s,%s,%s,%s,%s,%s)"
         result = cur.execute(sqlInsertArticle,(data['title'],data['author'],data['article'],data['published_time'],data['getTime'],data['url'],data['webname']))
     except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
     conn.commit()
     cur.close()
     conn.close()
     return result


def getSinaArticle(url,webname):
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

    #解析内容时如果有异常就捕获并返回空
    try:
        #读取网页内容并转换成树形文档结构
        soup = BeautifulSoup(html.read(),"lxml")

        #去除html注释
        for element in soup(text=lambda text: isinstance(text, Comment)):
            element.extract()

        #过滤JavaScript
        [s.extract() for s in soup('script')]

        #获取标题
        title = soup.find(id="main_title").get_text();
        # print(title)
        dict['title'] = title


        #获取发布时间
        published_time = soup.find(property="article:published_time")['content'];
        #2017-06-03T11:31:53+08:00   这种时间格式叫UTC时间格式...很恶心
        # print(published_time)
        UTC_FORMAT = "%Y-%m-%dT%H:%M:%S+08:00"
        dict['published_time'] = datetime.datetime.strptime(published_time, UTC_FORMAT)

        #获取作者
        author = soup.find(property="article:author")['content'];
        # print(author)
        dict['author'] = author

        #获取文章主体
        content = soup.find(id="artibody");
        img = content.find_all(class_="img_wrapper")
        #删除文档书中图片标签
        for del_img in img:
            del_img.decompose()

        #获取文章主体各个段落
        paragraph = soup.find(id="artibody").contents;

        #最终入库的文章内容
        article =""
        for child in paragraph:
            article += str(child)
        dict['article'] = article

        #文章抓取时间
        dict['getTime']=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    except:
        return None
    return dict

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

def GOSina(url,webname):
    #创建链接集合
    # pages = set()
    #创建字典用来储存函数的返回结果
    # dict={'url':url,'title':'','published_time':'','getTime':'','author':'','article':'','webname':webname}

    #创建请求头
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36",
             "Accept":"*/*"}

    #打开网页
    try:
        request = urllib2.Request(url,headers=headers)
        html = urlopen(request)
    except HTTPError as e:
        print(e)
    #读取网页内容并转换成树形文档结构
    soup = BeautifulSoup(html.read(),"lxml")
    conn = getConn();
    cur = conn.cursor()
    #声明一个数组用来存储入库的文章链接
    L = []
    for link in soup.findAll("a",href=re.compile(r'(.*?)(tech)(.*?)(\d{4}-\d{2}-\d{2})(/doc-ify)')):

        if 'href' in link.attrs:
            #提取href中的url，并规范格式去除分页参数
            xurl = re.compile(r'(.*?shtml)').search(link.attrs['href']).group(1)
            sqlQueryUrl="select * from tbl_peng_article where url='%s'"%xurl
            # print xurl
            result = cur.execute(sqlQueryUrl)
            conn.commit()
            if ( result == 0 ):
                # data = getSinaArticle(url,webname)
                rs = spiderSinaTech(xurl,webname)
                if( rs > 0 ):
                    logging.info("----URL has insert into database :%s"%xurl)
                    L.append(xurl)
                    time.sleep( 2 )
                elif( rs == -1):
                    logging.info("****URL content cannt be understand %s"%xurl)
            else :
                logging.info("&&&&URL already in database %s"%xurl)
    cur.close()
    conn.close()
    #如果不为空就返回最后一个url，为空则停止抓取
    if L:
        return L[-1]
    else:
        return 0

logging.info("begin spider sina tech")
url="http://tech.sina.com.cn/"
webname="sina"
x = GOSina(url,webname)
if x!= 0:
    GOSina(x,webname)

logging.info("end spider sina tech")

