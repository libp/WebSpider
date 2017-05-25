# -*- coding: utf-8 -*-    
     
import urllib2    
import urllib    
import re    
import thread    
import time
import codecs
import json
    
#----------- 加载处理浮生书店 -----------
class Spider_Model:    
        
    def __init__(self):    
        self.page = 100
        self.pages = []    
        self.enable = False    
    
    # 将所有的段子都扣出来，添加到列表中并且返回列表    
    def GetPage(self,page):    
        myUrl = "http://aladd.me/" + page+".htm"
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
        headers = {'User-Agent': user_agent}
        req = urllib2.Request(myUrl, headers = headers)
        myResponse = urllib2.urlopen(req)  
        myPage = myResponse.read()
        unicodePage = myPage.decode("utf-8")
        myItems = re.findall('<h1 class="entry-title".*?>(.*?)</h1>.*?<div class="article_text">(.*?)</div>',unicodePage, re.S)
        return myItems


    def LoadPage(self):    
        while self.enable:
            if len(self.pages) < 2:
                try:    
                    myPage = self.GetPage(str(self.page))
                    self.page += 1    
                    self.pages.append(myPage)
                except:    
                    print '无法链接浮生书店！'
            else:    
                time.sleep(5)


    def ShowPage(self,nowPage,page):
        i = 0
        f = codecs.open('C:\Users\Peng\Desktop\list.txt', 'ab+', 'utf-8')
        #可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建
        for i in range(0,len(nowPage)):
            if i < len(nowPage):
                f.write(nowPage[i][0])
                f.write("\r\n")
                f.write(nowPage[i][1])
                f.write("\r\n")
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
        #----------- 加载处理浮生书店 -----------
        while self.enable:    
            # 如果self的page数组中存有元素    
            if self.pages:    
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage,page)    
                page += 1


    
    
#----------- 程序的入口处 -----------    
print u"""  
---------------------------------------  
   程序：浮生书店爬虫
   版本：0.1
   作者：God
   日期：2016-08-21
   语言：Python 2.7  
   操作：输入quit退出阅读浮生书店
   功能：按下回车依次浏览今日的美文
---------------------------------------  
"""  
    
    
print u'请按下回车浏览今日的美文：'
raw_input(' ')
myModel = Spider_Model()    
myModel.Start()    