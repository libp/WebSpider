# -*- coding: utf-8 -*- 
__author__ = 'Peng'
import re
Url = "http://tech.sina.com.cn/mobile/n/n/2017-06-07/doc-ifyfuzny3696387.shtml?cre=techpagepc&mod=f&loc=1&r=1&doct=0&rfunc=100"
# pattern = re.compile(r'(.*?)(tech)(.*?)(\d{4}-\d{2}-\d{2})(/doc-ify)')
pattern = re.compile(r'(.*?shtml)')

match = pattern.search(Url)

if match:
    # 使用Match获得分组信息
    print match.group(1)