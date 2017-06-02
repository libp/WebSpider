# -*- coding: utf-8 -*-    
     
import urllib2    
import urllib    
import re    
import thread    
import time
import codecs
import json
    
#----------- 加载处理糗事百科 -----------    
class Spider_Model:    
        
    def __init__(self):    
        self.page = 1    
        self.pages = []    
        self.enable = False    
    
    # 将所有的段子都扣出来，添加到列表中并且返回列表    
    def GetPage(self,page):    
        myUrl = "http://m.qiushibaike.com/hot/page/" + page    
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
        headers = { 'User-Agent' : user_agent }   
        req = urllib2.Request(myUrl, headers = headers)   
        myResponse = urllib2.urlopen(req)  
        myPage = myResponse.read()
        # print myPage
        unicodePage = myPage.decode("utf-8")
        # 找出所有class="content"的div标记    
        #re.S是任意匹配模式，也就是.可以匹配换行符    
        myItems = re.findall('<div.*?class="content">(.*?)</div>',unicodePage,re.S)
        items = []
        # print myItems
        # print str(myItems).decode('string_escape')
        # print json.dumps(myItems, encoding="UTF-8", ensure_ascii=False)
        # for item in myItems:
        #     # item 中第一个是div的标题，也就是时间
        #     # item 中第二个是div的内容，也就是内容
        #     items.append([item[0].replace("\n",""),item[1].replace("\n","")])
        # print myItems
        # print str(myItems).decode('string_escape')
        # print str(myItems).encode("UTF-8")
        # print myItems[0]
        return myItems

    # 用于加载新的段子    
    def LoadPage(self):    
        # 如果用户未输入quit则一直运行    
        while self.enable:    
            # 如果pages数组中的内容小于2个
            # print len(self.pages)
            if len(self.pages) < 2:
                try:    
                    # 获取新的页面中的段子们    
                    myPage = self.GetPage(str(self.page))
                    self.page += 1    
                    self.pages.append(myPage)
                except:    
                    print '无法链接糗事百科！'    
            else:    
                time.sleep(5)
            
    # def ShowPage(self,nowPage,page):
    #     print u'第%d页' % page,json.dumps(nowPage, encoding="UTF-8", ensure_ascii=False)

    def ShowPage(self,nowPage,page):
        i = 0
        f = codecs.open('C:\Users\Peng\Desktop\list.txt', 'a+', 'utf-8')
        #可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建

        for i in range(0,len(nowPage)):
            if i < len(nowPage):
                print u'第%d页,第%d个故事' %(page,i) ,nowPage[i].replace("\n\n","")
                f.write(nowPage[i].replace("\n\n",""))
                f.write("\r\n")
                # f.write("\n")
                # windows的换行是\r\n，unix的是\n，mac的是\r
                i += 1
            else:
                f.close()
                break

            
    def Start(self):    
        self.enable = True    
        page = self.page
        print u'正在加载中请稍候......'
        # 新建一个线程在后台加载段子并存储    
        thread.start_new_thread(self.LoadPage,())
        #----------- 加载处理糗事百科 -----------    
        while self.enable:    
            # 如果self的page数组中存有元素    
            if self.pages:    
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage,page)    
                page += 1
                if page == 35:
                    exit()

    
    
#----------- 程序的入口处 -----------    
print u"""  
---------------------------------------  
   程序：糗百爬虫  
   版本：0.3  
   作者：why  
   日期：2014-06-03  
   语言：Python 2.7  
   操作：输入quit退出阅读糗事百科  
   功能：按下回车依次浏览今日的糗百热点  
---------------------------------------  
"""  
    
    
print u'请按下回车浏览今日的糗百内容：'    
raw_input(' ')    
myModel = Spider_Model()    
myModel.Start()    