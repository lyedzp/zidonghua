#coding=utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.youdao.com')
# 获得所有cookie信息
# print(driver.get_cookies())
# 添加cookie信息并打印
driver.add_cookie({'name':'lye','value':'1233'})
for cookie in driver.get_cookies():
    print('-->%s-->%s'%(cookie['name'],cookie['value']))

