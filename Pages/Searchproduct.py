from Locators.Locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from Utilities.Genericfunctions import GenericFunction
class SearchproductTest():
    
    def __init__(self,driver):
        self.driver = driver
        self.shop_all_product_list_id = Locators.shop_all_product_list_id
        self.select_kitche_tool_category_label = Locators.select_kitche_tool_category_label
        self.select_furniture_category_by_xpath = Locators.select_furniture_category_by_xpath
        self.select_sofas_as_furniture_category_by_xpath = Locators.select_sofas_as_furniture_category_by_xpath   
        self.select_sofa_type_by_xpath = Locators.select_sofa_type_by_xpath
        
    def shopByCateogry(self):
        mouse_action = GenericFunction(self.driver)
        element = self.driver.find_element_by_id("nav-link-shopall")
        mouse_action.hoveon_mouse_action(element)
        print("hover on all product list")     
        try:
            element1 = self.driver.find_element_by_xpath(self.select_kitche_tool_category_label)
            mouse_action.hoveon_mouse_action(element1)
            print("hover on kitchen tool list")
            mouse_action.explicit_wait_for_element(By.XPATH, self.select_furniture_category_by_xpath)
            print("navigate to furniture page")
        except TimeoutException:   
            print("Not able to navigate to furniture page") 
            
    def select_sofas_as_furniture_cateogry(self):
        element = self.driver.find_element_by_xpath(self.select_sofas_as_furniture_category_by_xpath)
        GenericFunction.click_on_element(self, element) 
    
    def select_sofas_by_type(self):  
        sofas_type = self.driver.find_element_by_xpath(self.select_sofa_type_by_xpath)
        GenericFunction.click_on_element(self, sofas_type)