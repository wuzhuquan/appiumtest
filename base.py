import os
import unittest
import log_config
from appium import webdriver
from time import sleep
import get_driver
from get_element import Element
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ChatTest(unittest.TestCase,Element):
    logging = log_config.getlogger("")
    def setUp(self):
        self.driver = get_driver.get_driver()


    def tearDown(self):
        self.driver.quit()

    def test_chat(self):

        el = self.get_id("main_too_keen")
        el.click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
