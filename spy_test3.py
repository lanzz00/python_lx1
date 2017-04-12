#coding = utf-8

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

print("设置浏览器的宽X高")
driver.set_Window_size(400,800)
driver.quit