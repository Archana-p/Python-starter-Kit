
from test.test_enum import threading
from selenium.common.exceptions import TimeoutException
import random
import os
import logging


class Utilites:
    
    #this function is used to get current therad ID
    def get_current_therad_id(self):
        try:
            return "Thread:"+ threading.currentThread().ident
            logging.info("current therad id return")
        except TimeoutException:
            logging.error("Current Thread ID not found")
            
  
    def random_number_generator(self):
        #it will generate random number between 1 to 1000
        try:
            random_number = random.randint(1,1000)
            return random_number
            logging.info("random number return")
        except ArithmeticError:
            logging.error("Random Number generation Failed")
      
    def convert_to_string(self,value):
        #this function will convert object to string argument will be any datatype
        try:
            return str(value)
            logging.info("Object is converted to string")
        except ValueError:
            logging.error("Invalid argument is passed")
    
    def convert_list_to_array(self,my_list):
        #this function has input as list and output will be array
        try:
            array = []
            for l in my_list:
                array += l      
            return array
            logging.info("List is converted to array")
        except TimeoutException:
            logging.error("list is not converted into array")
    
    
    def convert_2D_array_to_list(self,input_array):
        #this function will take 2D array as input and will retrun list in output
        try:
            my_list = input_array.tolist()
            return  my_list
            logging.info("2D array converted to list successfully")
        except TimeoutException:
            logging.error("Converion of 2D array to list failed")
    
    
    def get_current_dir_path(self):
        #get current directory path
        try:
            dirpath = os.getcwd()
            logging.info("Current Directory is:"+dirpath)
            return dirpath
        except:
            logging.error("Path not found")
    
    def get_current_dir_folder_name(self):
        #get current folder name
        try:
            dirpath = os.getcwd()
            foldername = os.path.basename(dirpath)
            logging.info("Directory name is:"+foldername)
            return foldername
        except:
            logging.error("Path not found")
    
    #this function is used to scroll down window by using javascript       
    def scroll_down_window(self):
        try:
            driver = self.driver
            logging.info("Scroll to the bottom of the page")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except TimeoutException:
            logging.error("window scrolling Failed")
            