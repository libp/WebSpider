# -*- coding: utf-8 -*- 
__author__ = 'Peng'
import logging
import sys
# 配置日志信息 输出到文件 filemode  有a和w
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='a')

# 配置日志信息 输出到控制台
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                stream=sys.stdout)












