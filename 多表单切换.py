#coding=utf-8
from selenium import webdriver
import os
driver = webdriver.Firefox()
# os.path.abspath是当前目录下的文件
filepath = 'file:///'+os.path.abspath('frame.html')
driver.get(filepath)
# 源码部分
'''
<body>
<div class="row-fluid"> 
    <div class="span10 well">
        <h3>frame</h3>
            <iframe id="if" name="nf" src="http://www.baidu.com" width="800" height="300"></iframe>
    </div>
</div>,由源码可看出百度首页是通过iframe表单嵌入到页面上的，因此在页面上直接定位百度首页输入框肯定定位不到，所以要先通过switch_to_frame
找到id为if的<iframe>标签，再去定位百度输入框
'''
# 切换到iframe
driver.switch_to.frame('if')
# 再去定位输入框
driver.find_element_by_id('kw').send_keys('python')


# 注意：switch_to.frame默认取表单的id或者name,如果表单没有id或者name,可以用xpath定位到表单，再传入switch_to.frame中,如下
'''
getFrame=driver.find_element_by_xpath('//div[@class="span10 well"]/iframe')
driver.switch_to.frame('getFrame')
'''

#switch_to.parent_frame(),跳出当前表单

