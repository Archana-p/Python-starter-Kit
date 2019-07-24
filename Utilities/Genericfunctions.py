import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
class GenericFunction():
    def __init__(self,driver):
        self.driver = driver
    
    def send_value_to_textbox(self,value,element):
        element.send_keys(value)
        
    def click_on_element(self,element): 
        element.click()
        
    def wait(self):
        time.sleep(5)       
        
    def hoveon_mouse_action(self,element):
        action = ActionChains(self.driver);
        action.move_to_element(element).perform();
        
    def explicit_wait_for_element(self,locator_method ,locator):
        myElem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator_method, locator)))
        myElem.click()
    
    def select_element_from_dropdown_by_value(self,element,value):
        s1 = Select(self.driver.find_element_by_id(element))
        s1.select_by_value(value)
        
    def press_keyboard_enter_key(self,keys,element,value):
        element.send_keys(value,keys)
        
    def check_element_selected(self,element):
        element.is_selected()
    
    def check_element_displayed(self,element):
        element.is_displayed()()
    
    def check_element_enabled(self,element):
        element.is_enabled()()
      
    def navigate_to_previous_page(self):
        self.driver.execute_script("window.histroy.go(-1)")
    
    def refresh_current_page(self):
        self.driver.refresh()
        
    def switch_window(self,window_handle):
        self.driver.switch_to_window(window_handle)
        
    def get_text(self,element):
        element.text()
        
    def get_attribute_value(self,element,attr_name):
        element.get_attribute_value(attr_name)
        