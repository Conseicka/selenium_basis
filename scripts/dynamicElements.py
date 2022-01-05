import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class DynamicElements(unittest.TestCase):

    def setUp(self):
        serv = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = serv)
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/disappearing_elements')


    def test_name_elements(self):
        driver = self.driver

        options = []
        menu = 5
        tries = 1
        counter = 0
        while len(options) < 5:
            options.clear()
            counter += 1

            for i in range(menu):
                try:
                    option_name = driver.find_element(By.XPATH,f"/html/body/div[2]/div/div/ul/li[{i+1}]/a")
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f'Option number {i +1} was NOT FOUND')
                    tries += 1
                    driver.refresh()
            if counter == 20:
                break
        print(f"Finished in {tries} tries")



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
