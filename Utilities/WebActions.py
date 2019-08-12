import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException
import logging


class WebActions:
    
    
    def __init__(self,driver):
        self.driver = driver
    
    #this function will send value to text box argument value is some text and element is text box object where we are sending value
    #value = "ABC" 
    #element will be the locator 
    def send_value_to_textbox(self,value,element):
        try:
            element.send_keys(value)
            logging.info("value send to text box")
        except ElementNotInteractableException:
            logging.error("Element not found")
            
    #this function will click on element where element is object on
    # which we are going to perform click operation    
    #element will be the locator of page
    def click_on_element(self,element): 
        try:
            element.click()
            logging.info("Clicked successfully")
        except ElementNotInteractableException:
            logging.error("Element not found to perform click action")
    
    #this functions is used to apply some wait in between the functions  
    def wait(self):
        try:
            time.sleep(5) 
            logging.info("wait for five seconds")  
        except TimeoutException:
            logging.error("wait Failed")   
    
    #mouse hover action is performed by using this function where element
    #is page object on which we are going to hover  
    def hover_on_mouse_action(self,element):
        try:
            action = ActionChains(self.driver);
            action.move_to_element(element).perform();
            logging.info("hover on mouse action performed successfully")
        except ElementNotInteractableException:
            logging.error("Element not found for hover action")
        
    #this function will select the element from drop down by using value .Element is drop           down locator
    def select_element_from_dropdown_by_value(self,element,value):
        try:
            s1 = Select(self.driver.find_element_by_id(element))
            s1.select_by_value(value)
            logging.info("element is selected from dropdown")
        except ElementNotInteractableException:
            logging.error("Element not found")
     
    #this function will perform  keyboard event where key is keyboard key  element is page object and value is the text that we want.           
    def press_keyboard_enter_key(self,keys,element,value):
        try:
            element.send_keys(value,keys)
            logging.info("keyboard key is pressed")
        except:
            logging.error("keyboard is not pressed")
            
    #this function will check if element is selected or not where element is object that we want to select
    def check_element_selected(self,element):
        try:
            element.is_selected()
            logging.info("element is selected")
        except ElementNotInteractableException:
            logging.error("Element is not selected")
            
    #this function will check if element is displayed or not where element is page object
    def check_element_displayed(self,element):
        try:
            element.is_displayed()
            logging.info("Element is displayed")
        except ElementNotInteractableException:
            logging.error("Element is not displayed")
            
    #this function will check if element is enabled or not where element is page object
    def check_element_enabled(self,element):
        try:
            element.is_enabled()
            logging.info("Element is enabled")
        except ElementNotInteractableException:
            logging.error("Element not found")
                            
    #this function will take user to previous page
    def navigate_to_previous_page(self):
        try:
            self.driver.execute_script("window.histroy.go(-1)")
            logging.info("Navigate to previous page")
        except TimeoutException:
            logging.error("Page not fund")
    
    #this function will refresh the current page       
    def refresh_current_page(self):
        try:
            self.driver.refresh()
            logging.info("page refreshed successfully")
        except:
            logging.error("Page refresh failed")
    
    #this function will switch the window
    def switch_window(self,window_handle):
        try:
            self.driver.switch_to_window(window_handle)
            logging.info("switch window successfully")
        except:
            logging.error("Switch window failed")
            
    #this function is used to extract the text from element   
    def get_text(self,element):
        try:
            element.text()
        except ElementNotInteractableException:
            logging.error("Text is not present")
    
    #this function is used to extract the  attribute value from element   
    def get_attribute_value(self,element,attr_name):
        try:
            element.get_attribute_value(attr_name)
        except ElementNotInteractableException:
            logging.error("Attribute value is not present")
    
    #by using this function we can find the size of element   
    def get_element_size(self,element):
        try:
            #output will be in the form of dict {hight:100,width:200}
            element.get_size()
        except ElementNotInteractableException:
            logging.error("element not found")
    
    #this function is used to submit the form   
    def submit_form(self,element):
        try:
            element.submit()
        except ElementNotInteractableException:
            logging.error("Element not found")
    
    #this function is used to drag and drop the element    
    def drag_and_drop_element(self,source_element,target_element):
        try:
            driver = self.driver
            action_chains = ActionChains(driver)
            action_chains.drag_and_drop(source_element, target_element)
        except ElementNotInteractableException:
            logging.error("Element Not Found")
        
    def add_cookies(self,cookie):
        #cookie is the variable which stored actual value like cookie:{'name':'foo','value':'bar'}
        try:
            self.driver.add_cookie(cookie)
            logging.info("cookies added successfully")
        except:
            logging.error("cookies not added successfully")
    
    def get_all_cookies(self):
        #this function will return all the cookies from current url
        self.driver.get_cookies()   
    

            