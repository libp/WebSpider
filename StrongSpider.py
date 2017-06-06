# -*- coding: utf-8 -*-


__author__ = 'Peng'
from bs4 import BeautifulSoup
from urllib2 import urlopen,HTTPError
import MySQLdb
import json
import datetime


def spiderIt():
     conn = getConn();
     cur = conn.cursor()
     sqli="insert into tbl_peng_article (title,author,content,createTime,url,webname) values (%s,%s,%s,%s,%s,%s)"

     url="http://tech.sina.com.cn/d/s/2017-06-03/doc-ifyfuzny2810237.shtml"
     webname="sina"
     #decode("unicode-escape") 将输出的unicode字典转换成汉字
     # print(getArticle(url).decode("unicode-escape"))
     data = getArticle(url,webname)
     # data = json.loads(dict)
     try:
         result = cur.execute(sqli,(data['title'],data['author'],data['article'],data['published_time'],data['url'],data['webname']))
         print result
         conn.commit()
     except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
     cur.close()
     conn.close()


def getArticle(url,webname):
    #创建字典用来储存函数的返回结果
    dict={'url':url,'title':'','published_time':'','author':'','article':'','webname':webname}
    #打开网页
    try:
        dict['url']=url
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    #读取网页内容并转换成树形文档结构
    soup = BeautifulSoup(html.read(),"lxml")
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


spiderIt()



