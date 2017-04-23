from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.baidu.com/")

assert "百度" in driver.title

elem = driver.find_element_by_id("su")
elem.send_keys('seleniumhq' + Keys.RETURN)

driver.quit()
'''
elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()
'''
