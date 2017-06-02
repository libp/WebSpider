__author__ = 'Peng'
import urllib2
req = urllib2.Request('http://aladd.me/100.htm')
response = urllib2.urlopen(req)
the_page = response.read()
print the_page