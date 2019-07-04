#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Firefox()
driver.get('https://www.mepai.me/recommend')
driver.maximize_window()

# # 找到需要右键的元素
# right_click=driver.find_element_by_class_name('mp-icon')
# driver.implicitly_wait(5)
# # 执行右键操作
# ActionChains(driver).context_click(right_click).perform()

# # 找到需要鼠标虚浮的元素
# above = driver.find_element_by_link_text('关于')
# # 将鼠标悬浮在关于上面
# ActionChains(driver).move_to_element(above).perform()

# 定位到需要拖拽的元素的原始位置,这里没得合适的网址，无法测试
# element = driver.find_element_by_id('xxx')
# # 定位元素要移动到的目标位置
# target = driver.find_element_by_id('ccc')
# ActionChains(driver).drag_and_drop(element,target).perform()
