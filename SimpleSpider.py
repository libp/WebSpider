# -*- coding: utf-8 -*-
__author__ = 'Peng'
import urllib2
# response = urllib2.urlopen('http://www.xxbiquge.com/5_5637/1072794.html')
# html = response.read()
sName='begin.html'
f = open('C:\Users\Peng\Desktop\\'+sName,'w+')  #打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
m = urllib2.urlopen('http://www.xxbiquge.com/5_5637/1072794.html').read()
f.write(m)
f.close()
print m
# fo = open(sName, "r+")
# str = fo.read(10);
# print "读取的字符串是 : ", str




