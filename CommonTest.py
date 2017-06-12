# -*- coding: utf-8 -*- 
__author__ = 'Peng'

import ConfigParser
#读取配置
def getConfig():
    config = ConfigParser.ConfigParser()
    config.readfp(open("config.ini"), "r")
    print config.get("mysql", "port")


getConfig()
