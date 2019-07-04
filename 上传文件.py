#coding=utf-8
from selenium import webdriver
import os
driver = webdriver.Firefox()
filename = 'file:///'+os.path.abspath('upfile.html')
driver.get(filename)
# 方式一，直接定位到input标签，然后send_keys
# driver.find_element_by_name('file').send_keys(r'D:\\1.png')

#方式二，如果找不到input标签，要操作windows控件就要借助三方工具Autolt
driver.find_element_by_name('file').click()
os.system('D:\\upfile.exe')