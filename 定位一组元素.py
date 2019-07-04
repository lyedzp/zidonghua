#coding=utf-8
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://localhost:63342/untitled2/test.html?_ijt=70462o6qegg03hvehh5ccn7gm2")
# # 选择页面上所有tag name为input的元素
# inputs = driver.find_elements_by_tag_name('input')
# # 然后从中过滤出type为checkbox的元素，单机勾选
# for i in inputs:
#     if i.get_attribute('type') == "checkbox":
#         i.click()
#         sleep(2)
# driver.quit()



# 如果只想选中这组元素中的某一个多选框，比如选择第二个,pop()时最后一个，pop(0)第一个,pop(1)第二个
inputs = driver.find_elements_by_xpath('//input[@type="checkbox"]')
inputs.pop(1).click()
