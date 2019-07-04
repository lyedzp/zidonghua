#coding=utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
# 截取当前窗口，并指定截图保存位置
driver.get_screenshot_as_file('D://4_shot.png')