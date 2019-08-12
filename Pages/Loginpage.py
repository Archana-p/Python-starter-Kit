from Locators.Locators import Locators
from Utilities.WebActions import WebActions
from selenium.webdriver.common.keys import Keys
import logging


class LoginPage:
    
    def __init__(self,driver):
        self.driver = driver
    
    #this function will navigte user to login page   
    def Gotologinpage(self):
        try:
            element = self.driver.find_element_by_id(Locators.SignIn_Button_id)
            WebActions.click_on_element(self, element)
            logging.info("Navigate to login page successfully")
        except:
            logging.error("Navigation of login page Failed")
    
    #this function will pass the value for user name in text box      
    def enterusername(self,username):
        try:
            element = self.driver.find_element_by_id(Locators.Username_TextBox_id)
            WebActions.send_value_to_textbox(self, username, element)
            logging.info("User name entered successfully")
        except:
            logging.error("entering user name value failed")
    
    #this function will click on the next login page button    
    def clickfornextloginpage(self):
        try:
            element = self.driver.find_element_by_id(Locators.Continue_Button_id)
            WebActions.click_on_element(self, element)
            logging.info("Navigate to next login page successfully")
        except:
            logging.error("Navigation to next login page is failed")
    
    #this function is used to enter password in text box       
    def enterpassword(self,password):
        try:
            element = self.driver.find_element_by_id(Locators.Password_TextBox_id)
            WebActions.send_value_to_textbox(self, password, element)
            logging.info("Password value entered successfully")
        except:
            logging.error("Entering password value Failed")
    
    #click on login button              
    def clickonloginbutton(self):
        try:
            element = self.driver.find_element_by_id(Locators.Login_button_id)
            WebActions.click_on_element(self, element)
            logging.info("clicked on login button successfully")
        except:
            logging.error("Clicked on login button Failed")

    #this function will select the category from the dropdown
    def select_category_from_dropdown(self):
        try:
            WebActions.select_element_from_dropdown_by_value(self, Locators.select_dropdown_option_id, "search-alias=mobile-apps")
            element = self.driver.find_element_by_id(Locators.search_text_box_id)
            WebActions.press_keyboard_enter_key(self,Keys.ENTER,element,"Mobile")
            logging.info("category selected from drop down")
        except:
            logging.error("category not selected from drop down")
        