#coding=utf-8
from selenium import webdriver
from time import sleep
import os
driver = webdriver.Firefox()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(5)
# 获得百度搜索页的窗口句柄,current_window_handle:获得当前窗口句柄
search_handle = driver.current_window_handle
# 点击登录按钮
driver.find_element_by_link_text('登录').click()

# # 点击注册按钮
driver.find_element_by_link_text('立即注册').click()
sleep(3)
# 获取所有窗口句柄
handles = driver.window_handles
# 遍历所有句柄,如果不是搜索页句柄就是注册句柄(因为这里就只有搜索窗口和注册窗口)
for handle in handles:
    if handle!=search_handle:
        print('进来了')
        driver.switch_to.window(handle)
        driver.find_element_by_name('userName').send_keys('lyehjshdjshdsjhdjsdh')
        driver.close()
        sleep(3)

# 回到搜索窗口
for handle2 in handles:
    if handle2 == search_handle:
        print('回到搜索窗口')
        driver.switch_to.window(handle2)
        driver.find_element_by_id('kw').send_keys('python')
        driver.find_element_by_id('su').click()
        sleep(2)
driver.quit()