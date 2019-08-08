from Locators.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from Utilities.Genericfunctions import GenericFunction
import logging
from Utilities.Log import Log

class HomePage():
    
    #
    def __init__(self ,driver):
        self.driver=driver
        self.Nav_order_page_class_name = Locators.Nav_order_page_class_name
        self.Nav_home_page_class_name =Locators.Nav_home_page_class_name
        self.Logout_id =Locators.Logout_id
        self.logout_link_text = Locators.Logout_Link_Text
        self.logout_ccs_selector = Locators.logout_css_selector
     
    #this function will click on the orders link from the amazon page   
    def checkOrders(self):
        try:
            element = self.driver.find_element_by_id(self.Nav_order_page_class_name)
            GenericFunction.click_on_element(self, element)
            Log.write_info_to_log_file(self, "Element is clicked on successfully")
        except:
            Log.write_errors_to_log_file(self, "Element is not clicked successfully")
        
    
    #this function will take user back to home page   
    def navigatebacktoHomepage(self):
        try:
            element = self.driver.find_element_by_class_name(self.Nav_home_page_class_name)
            GenericFunction.click_on_element(self, element)
            logging.info("Navigate to Home Page successfully")
        except:
            logging.error("Navigation to Home Page is not successfully")
    
    #this function will sign out the user from the web site   
    def signoutfrompage(self):
        try:
            action = ActionChains(self.driver);
            element = self.driver.find_element_by_id("nav-link-accountList")
            action.move_to_element(element).perform();
            myElem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.Logout_id)))
            myElem.click()
            logging.info("sign out from website successfully")
        except TimeoutException:
            logging.error("Sign out failed")
            
    

