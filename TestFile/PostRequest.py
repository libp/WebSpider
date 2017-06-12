# -*- coding: utf-8 -*- 
__author__ = 'Peng'
#用于测试批量发送post请求
import requests
import json
# params={"message":{"name":"测试下批量post请求","content":"测试下批量post请求"}}
# params={"message":{"id":None,"to":None,"gender":1,"name":"xxxxxxxxxx","content":"xxxxxxxx","date":"","contact":""}}
params={"message":{"id":"","to":"","gender":1,"name":"xxx","content":"xxx","date":"","contact":""}}
# params={'message':{'id':'','to':'','gender':1,'name':'测试下批量post请求','content':'测试下批量post请求','date':'','contact':''}}
# params={'message':{'id':'','to':'','gender':1,'name':'xxx','content':'xx','date':'','contact':''}}
# params={'id':'','to':'','gender':1,'name':'xxx','content':'xx','date':'','contact':''}
# params={'message':{'gender':1,'name':'xxx','content':'xxx','date':'','contact':''}}
# params={"firstName":"John" , "lastName":"Doe"}
# jo = json.dumps(params)
print(params)
# print(jo)
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
r=requests.post("http://nigeerhuo.com:3000/message/insert",data=params,headers=headers)
# r=requests.post("http://nigeerhuo.com:3000/message/insert",{"message":{"id":"","to":"","gender":1,"name":"xxx","content":"xxx","date":"","contact":""}},headers=headers)

print(r.status_code)
# print(r.headers)
# print(r.content)
print(r.text)