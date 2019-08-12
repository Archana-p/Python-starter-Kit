from Locators.Locators import Locators
from Utilities.WebActions import WebActions
from selenium.webdriver.common.keys import Keys
from Utilities.Log import Log


class LoginPage:
    
    def __init__(self,driver):
        self.driver = driver
        
    
    #this function will navigate user to login page   
    def Gotologinpage(self):
        try:
            element = self.driver.find_element_by_id(Locators.SignIn_Button_id)
            WebActions.click_on_element(self, element)
            Log.write_info_to_log_file(self,"Login successfully")
        except:
            print("")
            #Log.write_errors_to_log_file(self, "Navigation of login page Failed")
    
    #this function will pass the value for user name in text box      
    def enterusername(self,username):
        try:
            element = self.driver.find_element_by_id(Locators.Username_TextBox_id)
            WebActions.send_value_to_textbox(self, username, element)
            Log.write_info_to_log_file(self ,"User name entered successfully")
        except:
            Log.write_errors_to_log_file(self,"Entering username failed")
    
    #this function will click on the next login page button    
    def clickfornextloginpage(self):
        try:
            element = self.driver.find_element_by_id(Locators.Continue_Button_id)
            WebActions.click_on_element(self, element)
            Log.write_info_to_log_file(self ,"Navigate to next Login page successfully")
        except:
            Log.write_errors_to_log_file(self,"Click on next login button Failed")
    
    #this function is used to enter password in text box       
    def enterpassword(self,password):
        try:
            element = self.driver.find_element_by_id(Locators.Password_TextBox_id)
            WebActions.send_value_to_textbox(self, password, element)
            Log.write_info_to_log_file(self,"Password value entered successfully")
        except:
            Log.write_errors_to_log_file(self,"Entering password failed")
    
    #click on login button              
    def clickonloginbutton(self):
        try:
            element = self.driver.find_element_by_id(Locators.Login_button_id)
            WebActions.click_on_element(self, element)
            Log.write_info_to_log_file(self ,"clicked on login button successfully")
        except:
            Log.write_errors_to_log_file(self, "clicked on login button failed")

    #this function will select the category from the dropdown
    def select_category_from_dropdown(self):
        try:
            WebActions.select_element_from_dropdown_by_value(self, Locators.select_dropdown_option_id, "search-alias=mobile-apps")
            element = self.driver.find_element_by_id(Locators.search_text_box_id)
            WebActions.press_keyboard_enter_key(self,Keys.ENTER,element,"Mobile")
            Log.write_info_to_log_file(self,"category selected from drop down")
        except:
            Log.write_info_to_log_file(self,"select categroy from dropdown failed")
        