# -*- coding: utf-8 -*-
__author__ = 'Peng'
import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')


# 伪装成浏览器访问
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
# }
# req = urllib2.Request(
#     url = 'http://secure.verycd.com/signin/*/http://www.verycd.com/',
#     data = postdata,
#     headers = headers
# )