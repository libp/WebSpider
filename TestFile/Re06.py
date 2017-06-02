# -*- coding: utf-8 -*-
import codecs
# content = u'你好，脚本之家 jb51.net'
# f = codecs.open('c:/1.txt', 'w', 'utf-8')
# f.write(content)

list = ['foo', 'bar']
list.append("item")
fl=open('c:/1.txt', 'w')
for i in list:
    fl.write(i)
    fl.write("\n")
fl.close()