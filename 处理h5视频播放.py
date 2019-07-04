#coding=utf-8
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('https://videojs.com/')
video = driver.find_element_by_id('preview-player_html5_api')
# 返回第一个视频播放文件的地址
url = driver.execute_script('return arguments[0].currentSrc',video)
print(url)

# 播放视频
print('start')
driver.execute_script('return arguments[0].play()',video)
# 播放2秒
sleep(2)
print('stop')
# 暂停视频
driver.execute_script('arguments[0].pause()',video)
