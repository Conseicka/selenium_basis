import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


class AssertionsTest(unittest.TestCase):
    """Find elements"""

    def setUp(self):
        serv = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = serv)
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')


    def tearDown(self):
        self.driver.quit()

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME,'q'))

    def test_languaje_option(self):
        self.assertTrue(self.is_element_present(By.ID,'select-language'))

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME,'q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME,'q')
        search_field.clear()

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as ve:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity = 2)
