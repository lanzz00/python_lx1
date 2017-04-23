#coding = utf-8

from selenium import webdriver
#y引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.baidu.com/")
double_click = driver.find_element_by_name("tj_settingicon")
ActionChains(driver).context_click(double_click).perform()
'''
above = driver.find_element_by_name("tj_settingicon")
ActionChains(driver).move_to_element(above).perform()
'''