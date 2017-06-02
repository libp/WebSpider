__author__ = 'Peng'
import urllib2
# response = urllib2.urlopen('http://www.qiushibaike.com/hot/page/2/?s=4905516')
headers = {
           'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
req = urllib2.Request(
        url = "http://www.qiushibaike.com/hot/page/2/?s=4905516" ,
        headers = headers
    )
myResponse  = urllib2.urlopen(req)
html = myResponse.read()

print html
