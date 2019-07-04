# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import login
import os
driver = webdriver.Firefox()
driver.get('https://www.mepai.me/')
login.logi(driver)
# 点击发布图片
push = driver.find_element_by_link_text('发布')
ActionChains(driver).move_to_element(push).perform()
driver.find_element_by_link_text('发布图片').click()
driver.find_element_by_class_name('btn-add').click()
# 调用.exe完成图片上传
os.system('d:\\7.exe')