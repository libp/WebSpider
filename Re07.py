__author__ = 'Peng'
import urllib2
import re
import json
# response = urllib2.urlopen('http://www.qiushibaike.com/hot/page/2/?s=4905516')
headers = {
           'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
req = urllib2.Request(
        url = "http://aladd.me/100.htm" ,
        headers = headers
    )
myResponse  = urllib2.urlopen(req)
html = myResponse.read()
unicodePage = html.decode("utf-8")
myItems = re.findall('<h1 class="entry-title".*?>(.*?)</h1>.*?<div class="article_text">(.*?)</div>',unicodePage, re.S)

# myItems = re.findall('<div class="article_text">(.*?)</div>',unicodePage,re.S)
#myItems输出的是一个列表，列表中包含一个元组
print myItems
print len(myItems)
print json.dumps(myItems[0], encoding="UTF-8", ensure_ascii=False)
print json.dumps(myItems[0][0], encoding="UTF-8", ensure_ascii=False)
print json.dumps(myItems[0][1], encoding="UTF-8", ensure_ascii=False)
