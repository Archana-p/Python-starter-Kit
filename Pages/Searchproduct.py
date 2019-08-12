from Locators.Locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from Utilities.WebActions import WebActions
from Waits.waits import Waits
import logging


class SearchproductTest():
    
    def __init__(self,driver):
        self.driver = driver
        
    #  this function will search the category 
    def shopByCateogry(self):
        driver = self.driver
        mouse_action = WebActions(self.driver)
        waits = Waits(driver)
        #WebActions.wait(self)
        element = self.driver.find_element_by_id("nav-link-shopall")
        WebActions.wait(self)
        element = waits.wait_for_element_presence(By.ID, "nav-link-shopall")
        mouse_action.hover_on_mouse_action(element)
        logging.info("hover on all product list")   
        try:
            element1 = self.driver.find_element_by_xpath(Locators.select_kitche_tool_category_label)
            WebActions.wait(self)
            mouse_action.hover_on_mouse_action(element1)
            logging.info("hover on kitchen tool list")
            waits.wait_for_element_presence(By.XPATH, Locators.select_furniture_category_by_xpath).click()
        except TimeoutException:   
            logging.info("Not able to navigate to furniture page") 
    
    #this function will select sofas from furniture category      
    def select_sofas_as_furniture_cateogry(self):
        try:
            element = self.driver.find_element_by_xpath(Locators.select_sofas_as_furniture_category_by_xpath)
            WebActions.click_on_element(self, element) 
            logging.info("sofas as furniture category selected")
        except TimeoutException:
            logging.info("selection of furniture category failed")
    
    #this function will select one of the type of sofa from furniture category      
    def select_sofas_by_type(self):  
        try:
            sofas_type = self.driver.find_element_by_xpath(Locators.select_sofa_type_by_xpath)
            WebActions.click_on_element(self, sofas_type)
            logging.info("sofa type selected successfully")
        except:
            logging.error("sofas type not selected")