# -*- coding: utf-8 -*-
__author__ = 'Peng'
import string, urllib2
from urllib2 import Request, urlopen, URLError, HTTPError

#捕获异常后会继续处理
def aladd():
    for i in range(100, 500):
        sName = string.zfill(i,5) + '.html'#自动填充成六位的文件名
        print '正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......'
        try:
            m = urllib2.urlopen('http://aladd.me/' + str(i)+'.htm').read()
            f = open('D:\\aladd\\'+sName,'w+')  #打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
            f.write(m)
            f.close()
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
#调用
aladd()




