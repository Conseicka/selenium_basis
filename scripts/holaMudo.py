import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

#Unittest (PyTest)
#Test Fixture: Preparaciones para antes y despues de la prueba
#Test Case: Unidad de codigo a probar
#Test Suite: Coleccion de Test Cases
#Test Runner: Orquestador de la ejecucion
#Test Report: Resumen de resultados

class HelloWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #Se prepara el entorno de la prueba
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        #Acciones automatizadas, caso de prueba
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_visit_wikipedia(self):
        #Acciones par finalizar la prueba
        self.driver.get('https://www.wikipedia.org')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name='hello-world-report'))
