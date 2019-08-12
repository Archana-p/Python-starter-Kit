
from test.test_enum import threading
from selenium.common.exceptions import TimeoutException
import random
import os
import logging


class Utilites:
    
    #this function is used to get current therad ID
    #output format will be 60040
    def get_current_therad_id(self):
        try:
            return "Thread:"+ threading.currentThread().ident
            logging.info("current therad id return")
        except TimeoutException:
            logging.error("Current Thread ID not found")
    #**********************************************************************************************#
    #it will generate random number between 1 to 1000        
    #output of this function will be random number - 539 number vary each time
    def random_number_generator(self):        
        try:
            random_number = random.randint(1,1000)
            return random_number
            logging.info("random number return")
        except ArithmeticError:
            logging.error("Random Number generation Failed")
    #*********************************************************************************************#  
    #this function will convert object to string argument will be any datatype
    #value will be anything like integer ,float
    def convert_to_string(self,value):      
        try:
            return str(value)
            logging.info("Object is converted to string")
        except ValueError:
            logging.error("Invalid argument is passed")
    
    
    #******************************************************************************#
    #get current directory path for python library 
    #output of this function will be 'C:\\Users\\archanap\\AppData\\Local\\Programs\\Python\\Python37-32'
    def get_current_dir_path(self):
       
        try:
            dirpath = os.getcwd()
            logging.info("Current Directory is:"+dirpath)
            return dirpath
        except:
            logging.error("Path not found")
    
    #******************************************************************************#
    ##get current folder name where python library is installed
    #output of this function will be 'Python37-32' 
    def get_current_dir_folder_name(self):        
        try:
            dirpath = os.getcwd()
            foldername = os.path.basename(dirpath)
            logging.info("Directory name is:"+foldername)
            return foldername
        except:
            logging.error("Path not found")
            
    #******************************************************************************#
    #this function is used to scroll down window by using JavaScript       
    def scroll_down_window(self):
        try:
            driver = self.driver
            logging.info("Scroll to the bottom of the page")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except TimeoutException:
            logging.error("window scrolling Failed")
            