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

#配置日志输出位置为控制台
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                stream=sys.stdout)

def spiderSina():
     conn = getConn();
     cur = conn.cursor()

     # url="http://tech.sina.com.cn/d/s/2017-06-03/doc-ifyfuzny2810237.shtml"
     url="http://tech.sina.com.cn/it/2017-06-07/doc-ifyfuzny3756083.shtml"
     webname="sina"
     #decode("unicode-escape") 将输出的unicode字典转换成汉字
     # print(getArticle(url).decode("unicode-escape"))
     data = getSinaArticle(url,webname)

     try:
         #入库之前判断url是否已经存在数据库中了
         sqlQueryUrl="select count(*) from tbl_peng_article where url='%s'"%data['url']
         queryUrlReuslt = cur.execute(sqlQueryUrl)
         if( queryUrlReuslt > 0 ):
             logging.info("URL already in database")
         else:
             sqlInsertArticle="insert into tbl_peng_article (title,author,content,createTime,getTime,url,webname) values (%s,%s,%s,%s,%s,%s,%s)"
             result = cur.execute(sqlInsertArticle,(data['title'],data['author'],data['article'],data['published_time'],data['getTime'],data['url'],data['webname']))
             if ( result > 0 ):
                 logging.info("insert success")
         conn.commit()
     except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
     cur.close()
     conn.close()


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
    #读取网页内容并转换成树形文档结构
    soup = BeautifulSoup(html.read(),"lxml")

    #去除html注释
    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()

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
    # print(article)
    dict['article'] = article
    # print json.dumps(dict)
    # date在转换成json的时候包括，需要重构date转换的函数
    # return json.dumps(dict)

    #文章抓取时间
    dict['getTime']=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
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


spiderSina()



