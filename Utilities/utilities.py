
from test.test_enum import threading
from selenium.common.exceptions import TimeoutException
import random
import os
from Utilities.Log import Log


class Utilites:
    
    #this function is used to get current therad ID
    #output format will be 60040
    def get_current_therad_id(self):
        try:
            Log.write_info_to_log_file(self,"current therad id return")
            return "Thread:"+ threading.currentThread().ident           
        except TimeoutException:
            Log.write_errors_to_log_file(self,"Current Thread ID not found")
    #**********************************************************************************************#
    #it will generate random number between 1 to 1000        
    #output of this function will be random number - 539 number vary each time
    def random_number_generator(self,start_number,end_number):        
        try:
            random_number = random.randint(start_number,end_number)
            Log.write_info_to_log_file(self,"random number return")
            return random_number          
        except ArithmeticError:
            Log.write_errors_to_log_file(self,"Random Number generation Failed")
    #*********************************************************************************************#  
    #this function will convert object to string argument will be any datatype
    #value will be anything like integer ,float
    def convert_to_string(self,value):      
        try:
            Log.write_info_to_log_file(self,"Object is converted to string")
            return str(value)           
        except ValueError:
            Log.write_errors_to_log_file(self,"Invalid argument is passed")
    
    
    #******************************************************************************#
    #get current directory path for python library 
    #output of this function will be 'C:\\Users\\archanap\\AppData\\Local\\Programs\\Python\\Python37-32'
    def get_current_dir_path(self):
       
        try:
            dirpath = os.getcwd()
            Log.write_info_to_log_file(self,"Current Directory is:"+dirpath)
            return dirpath
        except:
            Log.write_errors_to_log_file(self,"Path not found")
    
    #******************************************************************************#
    ##get current folder name where python library is installed
    #output of this function will be 'Python37-32' 
    def get_current_dir_folder_name(self):        
        try:
            dirpath = os.getcwd()
            foldername = os.path.basename(dirpath)
            Log.write_info_to_log_file(self, "Directory name is:"+foldername)
            return foldername
        except:
            Log.write_errors_to_log_file(self,"Path not found")
            
    #******************************************************************************#
    #this function is used to scroll down window by using JavaScript       
    def scroll_down_window(self):
        try:
            driver = self.driver
            Log.write_info_to_log_file(self,"Scroll to the bottom of the page")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except TimeoutException:
            Log.write_errors_to_log_file(self,"window scrolling Failed")
            