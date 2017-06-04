# -*- coding: utf-8 -*- 
__author__ = 'Peng'
from bs4 import BeautifulSoup



soup = BeautifulSoup("http://tech.sina.com.cn/d/s/2017-06-03/doc-ifyfuzny2810237.shtml")



print soup.prettify()