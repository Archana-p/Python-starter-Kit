from Config import config
import unittest
import HtmlTestRunner
from Tests.Login import LoginTest
from BrowserType.BrowserType import BrowserType


class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        BrowserType.get_browser_value(cls, config.CHROME)
        #cls.driver.get(config.APPLICATION_URL)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    #called all the tests of login page from Login.py file
    def test_login_page(self):
        LoginTest.test_login_valid(self)
        LoginTest.test_search_valid_category(self)
        LoginTest.test_valid_logout(self)
        
    def suite(self):       
        suite = unittest.TestLoader()
        suite =suite.loadTestsFromModule(Test1)
        unittest.TextTestRunner().run(suite)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()   
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=config.HTML_REPORT_DIR))    
    #unittest.main()     