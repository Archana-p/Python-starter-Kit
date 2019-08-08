from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import logging

  
class Waits: 
    def __init__(self,driver):
        self.driver = driver
        
    def wait_for_element_presence(self,locator_method ,locator) :
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator_method, locator)))
            return element
            logging.info("Element is present")
        except TimeoutException:
            logging.error("Element is not present")
        
    def wait_for_element_visiblity(self,locator_method,locator):
        try:
            element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator_method,locator))
            return element
            logging.info("Element is visible")
        except ElementNotVisibleException:
            logging.error("Element not visible")
    
    def wait_for_element_invisiblity(self,locator_method,locator):
        try:
            element = WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(locator_method,locator))
            return element
            logging.info("Element Found")
        except TimeoutError:
            logging.error("Element not found Timeout error occured")
            
    def wait_for_element_clickablity(self,locator_method,locator):
        try:
            element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator_method,locator))
            return element
            logging.info("Element is present")
        except NoSuchElementException:
            logging.error("Element not Found Exception")
    
    def wait_for_element_to_find_by_text(self,locator_method,locator,inner_text):
        try:
            element=WebDriverWait(self.driver,10).unit(EC.text_to_be_present_in_element(locator_method,locator,inner_text))
            return element
            logging.info("Element is present")
        except:
            logging.error("Element Text Not Found")
    
    def wait_for_element_to_alert_is_present(self):
        try: 
            myElem = WebDriverWait(self.driver,10).until(EC.alert_is_present())
            myElem.switch_to_alert().accept()
        except TimeoutException:
            logging.error("Alert not appear")
            
            
    #waits method where return type is BOOLEAN
    def wait_for_element_presence_boolean(self,locator_method ,locator) :
        try:
            if (WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator_method, locator))):
                return True
        except TimeoutException:
            logging.error("Element is not present")
    
    
    