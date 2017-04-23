import unittest
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])

class googleTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(chrome_options=options)
        self.addCleanup(self.browser.quit)
    def testPageTitle(self):
        self.browser.get('http://www.baidu.com')
        self.assertIn('百度一下，你就知道', self.browser.title)
if __name__ == '__main__':
    unittest.main(verbosity=2)