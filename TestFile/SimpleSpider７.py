# -*- coding: utf-8 -*-
__author__ = 'Peng'
import urllib2
from urllib2 import URLError
import re
import datetime
import MySQLdb
import random
#捕获异常后会继续处理
def aladd():
    conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='root',
        db ='interesting',
        charset='utf8',
        )
    cur = conn.cursor()
    for i in range(105, 500):
        print '正在抄写第' + str(i) + '个故事'
        try:
            my_url='http://fushengshudian.com/' + str(i)+'.htm'
            req = getReq_multiTry(my_url)
            response = urllib2.urlopen(req)
            if (response.geturl() ==( 'http://fushengshudian.com/' + str(i)+'.htm')):
                m = response.read()
                unicodePage = m.decode("utf-8")
                myItems = re.findall('<h1 class="entry-title".*?>(.*?)</h1>.*?<div class="entry-content">'
                                     '.*?<p class="article_author".*?>(.*?)</p>.*?<div class="article_text">(.*?)</div><!-- .entry-content -->',unicodePage, re.S)
                if(len(myItems)==1):
                    sqli="insert into tbl_peng_article (title,author,content,createTime,num,clicks,abstract) values (%s,%s,%s,%s,%s,%s,%s)"
                    p= re.findall('<p>(.*?)</p>',myItems[0][2], re.S)
                    content=myItems[0][2].strip()     #去除文章末尾的空格和换行
                    abstract=p[0]+''+p[1]
                    createTime=getTime()
                    clicks=random.randint(10, 300)
                    num=i  #以后需要改进一下，这个num是数据库里编码最大的加一
                    try:
                        cur.execute(sqli,(myItems[0][0],myItems[0][1],content,createTime,num,clicks,abstract))
                        conn.commit()
                    except MySQLdb.Error,e:
                        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                else:
                    print "没有抓到文章内容"
            else:
                continue
        except URLError, e:
            if hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
            elif hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            else:
                print 'No exception was raised.'
        except IOError, e:
            print("File Error:"+str(e))

    cur.close()
    conn.close()

def getReq_multiTry(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    maxTryNum=10
    for tries in range(maxTryNum):
        try:
            req = urllib2.Request(url, headers = headers)
            # html=urllib2.urlopen(req).read()
            break
        except:
            if tries <(maxTryNum-1):
                continue
            else:
                break
    return req
#调用

def getTime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
aladd()




