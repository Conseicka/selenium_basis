import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class HomePageTests(unittest.TestCase):
    """Find elements"""

    def setUp(self):
        serv = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = serv)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_test_field(self):
        """Find elements by id"""
        search_field = self.driver.find_element(By.ID,"search")

    def test_search_text_field_by_name(self):
        """Find elements by name"""
        search_field = self.driver.find_element(By.NAME,"q")

    def test_search_text_field_class_name(self):
        """Find elements by class name"""
        search_field = self.driver.find_element(By.CLASS_NAME,"input-text")

    def test_search_button_enabled(self):
        """Find elements by class name"""
        button = self.driver.find_element(By.CLASS_NAME,"button")

    def test_conunt_of_promo_banner_images(self):
        """Find elements by class name"""
        banner_list = self.driver.find_element(By.CLASS_NAME,"promos")
        banner = banner_list.find_elements(By.TAG_NAME,'img')
        self.assertEqual(3, len(banner))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity = 2)
