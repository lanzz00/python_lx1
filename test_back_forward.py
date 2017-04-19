#coding = utf-8
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options=options)
first_url = 'https://www.baidu.com/'
print('now access %s' %(first_url))
driver.get(first_url)

second_url = "http://news.baidu.com/"
print('now access %s' %(second_url))
driver.get(second_url)

#返回（退回）到百度
print('back to  %s' %(first_url))
driver.back()

#前进到新闻页面
print('forward to  %s' %(second_url))
driver.forward()