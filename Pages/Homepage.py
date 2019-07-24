from Locators.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from Utilities.Genericfunctions import GenericFunction

class HomePage():
    
    def __init__(self ,driver):
        self.driver=driver
        self.Nav_order_page_class_name = Locators.Nav_order_page_class_name
        self.Nav_home_page_class_name =Locators.Nav_home_page_class_name
        self.Logout_id =Locators.Logout_id
        self.logout_link_text = Locators.Logout_Link_Text
        self.logout_ccs_selector = Locators.logout_css_selector
        
    def checkOrders(self):
        element = self.driver.find_element_by_id(self.Nav_order_page_class_name)
        GenericFunction.click_on_element(self, element)
        
    def navigatebacktoHomepage(self):
        element = self.driver.find_element_by_class_name(self.Nav_home_page_class_name)
        GenericFunction.click_on_element(self, element)
        
    def signoutfrompage(self):
        try:
            action = ActionChains(self.driver);
            element = self.driver.find_element_by_id("nav-link-accountList")
            action.move_to_element(element).perform();
            myElem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.Logout_id)))
            myElem.click()
        except TimeoutException:
            print ("loading took so much time")
            
        #self.driver.find_element_by_css_selector(self.logout_ccs_selector).click()

