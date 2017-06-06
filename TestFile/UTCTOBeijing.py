# -*- coding: utf-8 -*- 
__author__ = 'Peng'
import datetime
import time
import datetime
utc = '2014-09-18T10:42:16.126Z'
local = '2014-09-18 11:42:16'

UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
LOCAL_FORMAT = "%Y-%m-%d %H:%M:%S"
a = datetime.datetime.strptime(utc, UTC_FORMAT)
b = datetime.datetime.strptime(local, LOCAL_FORMAT)
print a
print b
print '...............'




def utc2local(utc_st):
    'UTC时间转本地时间（+8:00）'
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st

def local2utc(local_st):
    '本地时间转UTC时间（-8:00）'
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.datetime.utcfromtimestamp(time_struct)
    return utc_st

utc_time = datetime.datetime(2014, 9, 18, 10, 42, 16, 126000)
# utc = '2014-09-18T10:42:16.126Z'
utc = '2017-06-03T11:33:53+08:00'
# UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
UTC_FORMAT = "%Y-%m-%dT%H:%M:%S+08:00"
utc_time2 = datetime.datetime.strptime(utc, UTC_FORMAT)
print utc_time2
# utc转本地
local_time = utc2local(utc_time)
local_time2 = utc2local(utc_time2)
print local_time2
print local_time.strftime('%Y-%m-%d %H:%M:%S')
print local_time2.strftime('%Y-%m-%d %H:%M:%S')
# output：2014-09-18 18:42:16


# 本地转utc
utc_tran = local2utc(local_time)
print utc_tran.strftime('%Y-%m-%d %H:%M:%S')
# output：2014-09-18 10:42:16