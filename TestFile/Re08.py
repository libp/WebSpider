# -*- coding: utf-8 -*-
__author__ = 'Peng'
import urllib2
import re
import codecs
headers = {
           'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
req = urllib2.Request(
        url = "http://aladd.me/144.htm",
        headers = headers
    )
myResponse = urllib2.urlopen(req)
html = myResponse.read()
unicodePage = html.decode("utf-8")
myItems = re.findall('<h1 class="entry-title".*?>(.*?)</h1>.*?<div class="article_text">(.*?)</div>', unicodePage, re.S)
print len(myItems)
print myItems[0][0]
f = codecs.open('D:\\aladd\\'+myItems[0][0]+'.txt', 'a+', 'utf-8')  #打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

f.write(myItems[0][1])
f.close()