#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
from time import sleep
# driver = webdriver.Firefox()
# driver.get('https://www.baidu.com')
#
# # 绕过验证码登录思路：1、先在浏览器登录2、通过抓包工具抓到登陆后的cookie,百度必须的cookie就是BAIDUID和BDUSS
# # 因此将他们添加进来就ok,其他测试项目要问清楚开发必须的cookie是哪些
# driver.add_cookie({'name':'BAIDUID','value':'18975CF7CE164584688E61EBB6819324:SL=0:NR=10:FG=1; sug=3; sugstore=0; ORIGIN=0; bdime=0; delPer=0;'})
# driver.add_cookie({'name':'BDUSS','value':'V1YUpnclhzR0dyOFFhN0FPTzYyN2x0R3NjaU4yeWVOeW96NlBFb2pRNjZsT2RjRUFBQUFBJCQAAAAAAAAAAAEAAACDDmaHbHllZHpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALoHwFy6B8BcSF'})
# sleep(10)
# driver.refresh()

# 测试米拍网的绕过验证码登录,神奇！！！
driver = webdriver.Firefox()
driver.get('https://www.mepai.me')
driver.add_cookie({'name':'Hm_lvt_254b384aaf3a7d744bb98874f76ba7d0','value':'1556083551'})
driver.add_cookie({'name':'Hm_lpvt_254b384aaf3a7d744bb98874f76ba7d0','value':'1556090786'})
driver.add_cookie({'name':'PHPSESSID','value':'be3a92f97a56b515d051496ba0da12fe'})
driver.add_cookie({'name':'_csrf','value':'24396c7bca2c69124b3e66ab729ce0f14d337a86b4d7097979a70f9dc5bc0762a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Pjr6djAyvHEe_FF9fziEeg-XS2WDxbQL%22%3B%7D'})
driver.refresh()

# 点击发布图片
push = driver.find_element_by_link_text('发布')
ActionChains(driver).move_to_element(push).perform()
driver.find_element_by_link_text('发布图片').click()
driver.find_element_by_class_name('btn-add').click()
# 调用.exe完成图片上传
os.system('d:\\7.exe')
