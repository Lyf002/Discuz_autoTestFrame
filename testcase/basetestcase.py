import unittest
from framework.browser_engine import BrowserEngine
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browser=BrowserEngine()
        self.driver=browser.open_browser()

        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def tearDown(self):
        self.driver.quit()