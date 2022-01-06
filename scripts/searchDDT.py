import unittest, csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ddt import ddt, data, unpack


def get_data(file):
    rows = [] # list for input
    data_file = open(file,'r') # variable define file in read mode

    reader = csv.reader(data_file) # variable select library for read file
    next(reader, None)

    for i in reader:
        rows.append(i)
    return rows

@ddt
class DataDrivenTest(unittest.TestCase):

    def setUp(self):
        serv = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = serv)
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')


    @data(*get_data("./testdata.csv")) # call our function get_data
    @unpack

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements(By.XPATH, '//h2[@class="product-name"]/a')

        expected_count = int(expected_count)


        if expected_count > 0:

            self.assertEqual(expected_count, len(products))
        else:
            msg = self.driver.find_element(By.CLASS_NAME,'note-msg')
            self.assertEqual('Your search returns no results.', msg)
        print(f'Find {len(products)} products')

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
