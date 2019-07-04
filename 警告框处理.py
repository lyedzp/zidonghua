#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Firefox()
driver.get('https://www.baidu.com/')
seting = driver.find_element_by_link_text('设置')
# 将鼠标悬浮在设置上面
ActionChains(driver).move_to_element(seting).perform()
driver.find_element_by_link_text('搜索设置').click()
driver.find_element_by_link_text('保存设置').click()
sleep(2)
# # 接受警告框
# driver.switch_to.alert.accept()

# 关闭/取消警告框
# driver.switch_to.alert.dismiss()

# 获得警告框的文字
print(driver.switch_to.alert.text)

