#coding=utf-8
from time import sleep
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.maximize_window()
# 通过link定位文本链接
driver.find_element_by_link_text('新闻').click()
# 后退
driver.back()
#前进
driver.forward()
sleep(3)
# 刷新当前页面
driver.refresh()

# driver.find_element_by_id('kw').send_keys('python')
# driver.find_element_by_id('su').click()


driver.quit()