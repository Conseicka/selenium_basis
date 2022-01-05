import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls(unittest.TestCase):

    def setUp(self):
        serv = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = serv)
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/dynamic_controls')


    def test_dynamic_controls(self):
        driver = self.driver

        checkobox = driver.find_element(By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')
        checkobox.click()

        remove_add_buttom = driver.find_element(By.CSS_SELECTOR, "#checkbox > input[type=checkbox]")
        remove_add_buttom.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox > input[type=checkbox]")))
        remove_add_buttom.click()

        enable_disable_button = driver.find_element(By.CSS_SELECTOR, "#input-example > button")
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > button")))

        text_area = driver.find_element(By.CSS_SELECTOR, "#input-example > input[type=text]")
        text_area.send_keys('Platzi')

        sleep(2)

        enable_disable_button.click()



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
