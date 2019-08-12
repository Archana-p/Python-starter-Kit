from Locators.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from Utilities.WebActions import WebActions
from Utilities.Log import Log
from Waits.waits import Waits

class HomePage:
    
    #
    def __init__(self ,driver):
        self.driver=driver
     
    #this function will click on the orders link from the amazon page   
    def checkOrders(self):
        try:
            element = self.driver.find_element_by_id(Locators.Nav_order_page_class_name)
            WebActions.click_on_element(self, element)
            Log.write_info_to_log_file(self, "Element is clicked on successfully")
        except:
            Log.write_errors_to_log_file(self, "Element is not clicked successfully")
        
    
    #this function will take user back to home page   
    def navigatebacktoHomepage(self):
        try:
            element = self.driver.find_element_by_class_name(Locators.Nav_home_page_class_name)
            WebActions.click_on_element(self, element)
            Log.write_info_to_log_file(self,"Navigate to Home Page successfully")
        except:
            Log.write_errors_to_log_file(self,"Navigation to Home Page is not successfully")
    
    #this function will sign out the user from the web site   
    def signoutfrompage(self):
        try:
            action = ActionChains(self.driver);
            element = self.driver.find_element_by_id("nav-link-accountList")
            action.move_to_element(element).perform();
            myElem = Waits.wait_for_element_presence(self, By.XPATH, Locators.Logout_id)
            #myElem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.Logout_id)))
            myElem.click()
            Log.write_info_to_log_file(self,"sign out from website successfully")
        except TimeoutException:
            Log.write_errors_to_log_file(self,"Sign out failed")
            
    

