#-*- coding: UTF-8 -*-
__author__ = 'Peng'
import urllib2
req = urllib2.Request('http://www.runoob.com/python/pythdon-dicti2onary.html')

try:
    urllib2.urlopen(req)

except urllib2.URLError, e:

    print e.code  #403 禁止     处理方式：丢弃
    print e.read()