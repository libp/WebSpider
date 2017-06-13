# -*- coding: utf-8 -*-


__author__ = 'Peng'
import re
import ConfigParser
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#读取配置
def getConfig():
    config = ConfigParser.ConfigParser()
    config.readfp(open("config.ini"), "r")
    print config.get("mysql", "port")

# getConfig()

'''
用于判断标题是否符合要求
'''
def judgeTitle():
    # title = "荣耀9发布：2999元你又多了款摄新选择"
    title = "荣耀发布你元你又多了款摄新选择"
    print repr(title)
    # pattern = re.compile(u'[一二三四五六七八九十]+')  ok
    #  match = pattern.search(u''+title) ok

    pattern = re.compile(u'[一二三四五六七八九十]+')
    pattern2 = re.compile(r'\d+')
    match = pattern.search(u''+title)
    match2 = pattern2.search(title)
    if (match!=None) | (match2!=None):
        print "that is i want!"
    else:
        print "not match"
judgeTitle()

def judgeMode():
    # pattern = re.compile(r'[黄蓝绿黄]+[A-Z]{1}[A-Z0-9]{5}')
    # pattern = re.compile(r'[黄蓝绿黄]+')
    pattern = re.compile(u'[黄蓝绿黄]+')
    match = pattern.match(u'黄A12344')
    # match = pattern.search('xxx换又多了一款双摄新选A12344')
    if match:
        print "OK"
    else:
        print "not ok"

judgeMode()