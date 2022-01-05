import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class CompareProducts(unittest.TestCase):

    def setUp(self):
        serv = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = serv)
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get('https://www.google.com')


    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('Platzi')
        search_field.submit()

        time.sleep(3)
        driver.back()
        time.sleep(5)
        driver.forward()
        time.sleep(5)
        driver.refresh()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
