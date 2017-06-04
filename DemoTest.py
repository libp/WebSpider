# -*- coding: utf-8 -*- 
__author__ = 'Peng'

from bs4 import BeautifulSoup
from urllib2 import urlopen,HTTPError


try:
    html = urlopen("http://tech.sina.com.cn/d/s/2017-06-03/doc-ifyfuzny2810237.shtml")
except HTTPError as e:
    print(e)
soup = BeautifulSoup(html.read(),"lxml")

#获取页面中所有a元素
tags=soup.find_all('a')
for tag in tags:
    print(tag)

print("........................................")
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">你好Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup2 = BeautifulSoup(html,"lxml")
print soup2.select('p #link1')
print soup2.select('.story')


