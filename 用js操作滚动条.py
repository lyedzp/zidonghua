#coding=utf-8
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
# 设置窗口大小是为了让它出现水平滚动条和垂直滚动条
driver.set_window_size(1000,1000)
driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('su').click()
sleep(3)
# 调用js设置浏览器窗口的滚动条位置，100是水平滚动条左边距，450是垂直滚动条上边距
js = "window.scrollTo(100,450)"
driver.execute_script(js)