from Locators.Locators import Locators
from Utilities.Genericfunctions import GenericFunction

from selenium.webdriver.common.keys import Keys
class LoginPage():
    
    def __init__(self,driver):
        self.driver = driver
        self.signin_button_id = Locators.SignIn_Button_id
        self.Username_TextBox_id = Locators.Username_TextBox_id
        self.continue_button_id = Locators.Continue_Button_id
        self.Password_TextBox_id = Locators.Password_TextBox_id
        self.Login_button_id =Locators.Login_button_id
        self.select_dropdown_option_id = Locators.select_dropdown_option_id
        self.search_text_box_id = Locators.search_text_box_id
        
    def Gotologinpage(self):
        element = self.driver.find_element_by_id(self.signin_button_id)
        GenericFunction.click_on_element(self, element)
               
    def enterusername(self,username):
        element = self.driver.find_element_by_id(self.Username_TextBox_id)
        GenericFunction.send_value_to_textbox(self, username, element)
        
    def clickfornextloginpage(self):
        element = self.driver.find_element_by_id(self.continue_button_id)
        GenericFunction.click_on_element(self, element)
            
    def enterpassword(self,password):
        element = self.driver.find_element_by_id(self.Password_TextBox_id)
        GenericFunction.send_value_to_textbox(self, password, element)
        
        # password.send_keys("1992@poonam") 
           
    def clickonloginbutton(self):
        element = self.driver.find_element_by_id(self.Login_button_id)
        GenericFunction.click_on_element(self, element)
    
    def select_category_from_dropdown(self):
        GenericFunction.select_element_from_dropdown_by_value(self, self.select_dropdown_option_id, "search-alias=mobile-apps")
        element = self.driver.find_element_by_id(self.search_text_box_id)
        GenericFunction.press_keyboard_enter_key(self,Keys.ENTER,element,"Mobile")
        