#coding = utf-8

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://www.baidu.com/")

#获取输入框的尺寸
size = driver.find_element_by_id("kw").size
print(size)

#返回百度页底部备案信息
text = driver.find_element_by_id("cp").text
print(text)

#返回元素的属性值。可以是id,name,type或元素拥有其他的任意属性
atrr = driver.find_element_by_id("kw").get_attribute('type')
print(atrr)

#返回元素的结果是否可见，返回结果TRUE或FALSE
result = driver.find_element_by_id("kw").is_displayed()
print(result)