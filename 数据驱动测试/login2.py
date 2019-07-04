# 数据驱动测试也就是参数化。拿登录举例
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get('http://www.mepai.me')
f = open('F:\\move\\Desktop\\新建文件夹\\2.xlsx','r')
f.read()
fb = driver.find_element_by_link_text('发布')
ActionChains(driver).move_to_element(fb).perform()
driver.find_element_by_link_text('发布图片')
driver.find_element_by_name('mobile').send_keys('username')