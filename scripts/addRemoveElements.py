import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        serv = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = serv)
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/add_remove_elements/')

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

        sleep(1)

        for i in range(elements_added):
            add_button.click()
            sleep(1)

        for i in range(elements_removed):
            try:
                sleep(1)
                delete_button = driver.find_element(By.CLASS_NAME, 'added-manually')
                delete_button.click()
            except:
                print('You are traying to delete more elements than the exsistent')
                break

        if total_elements > 0:
            print(f'There are {total_elements} elements on screen')
        else:
            print(f'There are 0 elements on screen')



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
