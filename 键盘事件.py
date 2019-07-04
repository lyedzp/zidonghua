#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
# 模拟键盘向输入框输入
driver.find_element_by_id('kw').send_keys('python')
#模拟键盘全选输入框中的内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
sleep(3)
#模拟键盘剪切输入框中的内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
sleep(3)
#模拟键盘粘贴输入框中的内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
#模拟键盘向输入框输入空格
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
driver.find_element_by_id('kw').send_keys('的作用')

#通过回车键代替单击操作
driver.find_element_by_id('kw').send_keys(Keys.ENTER)