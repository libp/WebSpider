# -*- coding: utf-8 -*- 
__author__ = 'Peng'
import datetime
import time

timeStamp = time.time()

dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print otherStyleTime
