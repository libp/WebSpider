# -*- coding: utf-8 -*- 
__author__ = 'Peng'
from selenium import webdriver
from time import *
from pytesser import *
from PIL import Image

driver = webdriver.Chrome()
driver.get("https://180.2.35.192:7003/user/login.htm")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("gaorn")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("gaorn")
#//*[@id="codeImage"] //*[@id="imgObj"]
#验证码问题
# from pytesser import *
driver.find_element_by_id("codeImage").clear()
driver.save_screenshot('maPage.png')#截取当前网页，有我们需要的验证码
imgelement = driver.find_element_by_id("imgObj")#定位验证码
location = imgelement.location #获取验证码x，y轴坐标
size = imgelement.size #获取验证码长度
#写成我们需要截取的位置坐标
rangle = (int(location['x']),int(location['y'],int(location['x']+size['width']),int(location['y']+size['height'])))
i = Image.open('maPage.png') #打开截图
img = i.crop(rangle) #使用Image的crop函数，从截图中再次获取我们需要的区域
img = img.convert('L') #灰度转换
img.save('maBefore.png')
array = np.array(img) #转换成numpy数组便于运算
array[array>30] = 255 #np进行过滤
cimg = Image.fromarray(array) #优化后的数组变图片


cimg.save('maafter.png')
textcode = image_to_string(cimg) #使用pytesser转换图片
validate_code = textcode.strip().replace(' ',' ') #将空格剔除
driver.find_element_by_id("codeImage").send_keys(validate_code)


#选择框
from selenium.webdriver.support.select import Select
sel = driver.find_element_by_id("userType")
Select(sel).select_by_value('02')#内部用户
#Select(sel).select_by_value('04')#仓库用户

driver.find_element_by_xpath('//*[@id="loginForm"]/ul/li[6]/input[1]').click()
sleep(2)
driver.quit()