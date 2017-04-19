#coding = utf-8

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("shao nv shi dai")
driver.find_element_by_id("su").click()
driver.quit()