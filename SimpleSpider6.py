# -*- coding: utf-8 -*-
__author__ = 'Peng'
import urllib2
from urllib2 import URLError
import re
import codecs
import MySQLdb
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
            my_url='http://aladd.me/' + str(i)+'.htm'
            # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            # headers = {'User-Agent': user_agent}

            # req = urllib2.Request(my_url, headers = headers)
            req = getUrl_multiTry(my_url)
            response = urllib2.urlopen(req)
            #如果页面被跳转的话，就进入下一个循环
            if (response.geturl() ==( 'http://aladd.me/' + str(i)+'.htm')):
                m = response.read()
                unicodePage = m.decode("utf-8")
                myItems = re.findall('<h1 class="entry-title".*?>(.*?)</h1>.*?<div class="entry-content">.*?<p class="article_author".*?>(.*?)</p>.*?<div class="article_text">(.*?)</div></div>',unicodePage, re.S)
                # print len(myItems)
                if(len(myItems)==1):
                    f = codecs.open('D:\\aladd\\'+myItems[0][0]+'.txt','a+', 'utf-8')  #打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
                    f.write(myItems[0][1])
                    f.write(myItems[0][2])
                    sqli="insert into tbl_peng_article (title,author,content) values (%s,%s,%s)"
                    cur.execute(sqli,(myItems[0][0],myItems[0][1],myItems[0][2]))
                    conn.commit()
                    f.close()
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
                # everything is fine
        except IOError, e:
            print("File Error:"+str(e))

    cur.close()
    conn.commit()
    conn.close()

def getUrl_multiTry(url):
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
aladd()




