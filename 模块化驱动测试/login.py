#coding=utf-8
# 什么叫模块化驱动测试，就是把公共部分单独写成一个模块，减少代码冗余，例如登录，每个用例都要先登录，单独写成模块就只要在需要
from selenium import webdriver
#调用登录的地方调用就可以，就不需要再重复去写登录步骤
def logi(driver):
    driver1 = driver
    driver1.add_cookie({'name': 'Hm_lvt_254b384aaf3a7d744bb98874f76ba7d0', 'value': '1556083551'})
    driver1.add_cookie({'name': 'Hm_lpvt_254b384aaf3a7d744bb98874f76ba7d0', 'value': '1556090786'})
    driver1.add_cookie({'name': 'PHPSESSID', 'value': 'be3a92f97a56b515d051496ba0da12fe'})
    driver1.add_cookie({'name': '_csrf','value': '24396c7bca2c69124b3e66ab729ce0f14d337a86b4d7097979a70f9dc5bc0762a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Pjr6djAyvHEe_FF9fziEeg-XS2WDxbQL%22%3B%7D'})
    driver1.refresh()

