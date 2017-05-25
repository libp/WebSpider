# -*- coding: utf-8 -*-
#两个等价的re匹配,匹配一个小数
import re

a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)

b = re.compile(r"\d+\.\d*")

match11 = a.match('3.1415')
match12 = a.match('33')
match21 = b.match('3.1415')
match22 = b.match('33')

if match11:
    # 使用Match获得分组信息
    print match11.group()
else:
    print u'match11不是小数'

if match12:
    # 使用Match获得分组信息
    print match12.group()
else:
    print u'match12不是小数'

if match21:
    # 使用Match获得分组信息
    print match21.group()
else:
    print u'match21不是小数'

if match22:
    # 使用Match获得分组信息
    print match22.group()
else:
    print u'match22不是小数'