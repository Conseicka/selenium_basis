from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from HtmlTestRunner import HTMLTestRunner
from searchTests import HomePageTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(HomePageTests)

#contruimos la suite de pruebas
smoke_test = TestSuite([assertions_test, search_tests])

kwargs = {
    "output": "reports/smoke-report",
    "report_name": "smoke-report",
    "combine_reports": True,
    "add_timestamp": False
}

# ? create runner with the parameters and run
runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
