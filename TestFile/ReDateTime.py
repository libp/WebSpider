# -*- coding: utf-8 -*-
__author__ = 'Peng'
import urllib2
import re
import codecs
import random


href = 'http://tech.sina.com.cn/d/a/2017-05-22/doc-ifyfkqks4409930.shtml'
# x=re.compile(".*?doc-ify.*?")
x=re.compile(".*?2017-05-22.*?")
y=x.match(href)
print y.string
print y.group()

#先写好匹配规则，然后是匹配字符串里有没有符合规则的，有的话就输出


# 将正则表达式编译成Pattern对象
pattern = re.compile(r'(.*?)(tech)(.*?)(\d{4}-\d{2}-\d{2})(/doc-ify)')
xx = 'http://tech.sina.com.cn/d/a/2017-05-22/doc-ifyfkqks4409930.shtml'
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
# match = pattern.match(xx)
match = pattern.search(xx)

if match:
    # 使用Match获得分组信息
    print match.group(4)

L = [1,2,3,4]

length = len(L)
print length
print random.randint(0,length-1)
if L:
    print L[random.randint(0,length)-1]
else:
    print "yy"
