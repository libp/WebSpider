# -*- coding: utf-8 -*-
#两个等价的re匹配,匹配一个小数
import re

import sys

import json

b = re.compile(r"\d+\.\d*")
match21 = b.match('3.1415')
if match21:
    # 使用Match获得分组信息
    print match21.group()
else:
    print u'match21不是小数'

myPage=u"""<div class="content">
分享一个小表妹的…<br/>姑姑女儿今年10岁，听她说小表妹5，6岁的时候有次出去玩，身上没带钱，又不敢上公交车，就在公交站台一直哭啊哭…后来听姑姑说表妹回来得时候大冬天的哭的脸上都是鼻涕…公交师傅说求了她老半天她才愿意上车…满车人还以为公交师傅把她怎么样了…
</div>"""
reload(sys)
sys.setdefaultencoding('utf-8')
unicodePage = myPage.decode("utf-8")
#下面这句话的理解是，匹配div中任意字符但是不放到myItems中，后面那个（。*？）则会放到myItems中
#参考这个url：http://blog.csdn.net/cashey1991/article/details/8875213
myItems = re.findall('<div.*?class="content">(.*?)</div>',unicodePage,re.S)

print myItems
print str(myItems).decode('string_escape')
print json.dumps(myItems, encoding="UTF-8", ensure_ascii=False)



a = ['中文', 'ab']
 # unicode 字符串在内存中的形式，python 在命令行界面输出的数据，如果不是ASCII码，则会以十六进制形式输出。
print a
print str(a).decode('string_escape')

b = ["\n\n老婆用毛线织出方便面的味道\n\n", "\n\n我小姨问我：“今年交男朋友了吗？”<br/>我：“目前，我比较喜欢单身~”<br/>然后我弟那个贱人突然来了一句：“你要知道，单身和没人肯要是两回事。”\n\n", "\n\n刚刚侄儿让我拿五块钱给他买冰激凌，我没零钱就说等下给他！没想到他居然说这么抠，难怪天天赖在家嫁不出去！卧槽\n\n", "\n\n昨晚外甥女尿床，所以我没地方睡了，就睡地板上。半小时内我妈踩了我4次，表妹来拿东西回家踩了我2次，外甥女的玩具砸了我4次，然后我就没睡了\n\n", "\n\n接陌生来电:“你好，请问原油期货有没有兴趣啊”<br/>我回答:“有啊，所以我在阿拉伯买了几块油田”<br/>电话那头一片静默<br/>然后他挂了\n\n", "\n\n昨天正在玩手机，儿子突然把我手机夺去：你天天就知道玩手机，不能陪我玩会吗？<br/>我：可以呀！我们来玩个游戏吧，我来演皇帝，你演大臣。<br/>儿子兴奋的点点头。<br/>我：来人呀！<br/>儿子：臣在。<br/>我：把朕的手机拿来。<br/>儿子：………………\n\n", "\n\n去给儿子买座椅，我：老板座椅多少钱？老板：这个是一千的，看咱俩有缘收你三十算了。老板这逼装的我给你88分\n\n", "\n\n一天听邻居教育上幼儿园的儿子: 女人是善变的，小孩子是喜怒无常的，所以呢，幼儿园的恋情是靠不住的！\n\n", "\n\n爷爷没出过远门，从没坐过火车！昨天我哥从广州来电话说:“买了两张卧铺票，让我带着爷爷去广州玩一玩。”这下把爷爷激动的，不光一夜没怎么睡，就是去火车站，都要早去一会，说:“好不容易有出远门坐火车的机会，还是卧铺，怎么也要提前上车铺铺床！。。。\n\n", "\n\n记得当初拍结婚照，等了一个多小时才给媳妇化好妆，轮到我的时候连梳子都没用，抓了几下搞定。我问就这样？"]
b[0].replace("\n\n","")
print b[0]
print b[0].replace("\n\n","")



