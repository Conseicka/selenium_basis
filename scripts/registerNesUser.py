import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        serv = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = serv)
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver

        driver.find_element(By.XPATH,'/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element(By.LINK_TEXT,'Log In').click()

        create_account_button = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)

        submit_button = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')
        news_letter_subscription = driver.find_element(By.ID,'is_subscribed')
        confirm_password = driver.find_element(By.ID,'confirmation')
        password = driver.find_element(By.ID, 'password')
        last_name = driver.find_element(By.ID, 'lastname')
        first_name = driver.find_element(By.ID, 'firstname')
        middle_name = driver.find_element(By.ID, 'middlename')

        email_address = driver.find_element(By.ID, 'email_address')

        self.assertTrue(
            first_name.is_enabled()
            and middle_name.is_enabled()
            and last_name.is_enabled()
            and email_address.is_enabled()
            and news_letter_subscription.is_enabled()
            and password.is_enabled()
            and confirm_password.is_enabled()
        )

        first_name.send_keys('test')
        middle_name.send_keys('test')
        last_name.send_keys('test')
        email_address.send_keys('test@ttest.tom')
        password.send_keys('test')
        confirm_password.send_keys('test')
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
