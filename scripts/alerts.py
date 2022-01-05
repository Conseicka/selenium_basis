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
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        #es buena practica borrar el campo de busqueda antes de escribir en el
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element(By.CLASS_NAME, 'link-compare').click()
        driver.find_element(By.CLASS_NAME, 'link-compare').click()
        driver.find_element(By.LINK_TEXT, 'Clear All').click()

        #time.sleep(.5)
        alert = driver.switch_to.alert
        alert_text = alert.text

        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        alert.accept()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
