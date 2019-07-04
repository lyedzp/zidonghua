#coding=utf-8
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('http://www.youdao.com/')
driver.maximize_window()
driver.find_element_by_name('q').send_keys('jisdhsjdhsjdhjsdhjsdhjshd')
sleep(3)


# # 清除文本内容
driver.find_element_by_name('q').clear()

driver.find_element_by_name('q').send_keys('hello')
# submit相当于把回车
driver.find_element_by_name('q').submit()