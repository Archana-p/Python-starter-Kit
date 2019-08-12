import time
import logging
from datetime import datetime
from selenium.common.exceptions import TimeoutException

class DateAndTime:
    
    #this function will return current time in milli seconds output will be  current time in (E.g. 1565333087245) in millis
    @staticmethod
    def get_current_time_in_millis(self):
        try:
            current_milli_time = int(round(time.time()* 1000))
            logging.info("current time converted into millis")
            return current_milli_time           
        except TimeoutException:
            logging.error("current time is not converted into millis")
    
    #this function will written current date and time and format of output will be '09/08/2019 12:16:03'
    @staticmethod
    def get_current_date_and_time(self):
        try:
            current_date_time = datetime.now()
            current_date_time_format = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
            logging.info("get current Date and Time in '09/08/2019 12:16:03' format")
            return current_date_time_format            
        except TimeoutException:
            logging.error("output for current date and time is not getting")
    
    #this function will written current date and time in different format and output of this function will be 'August 09,2019 12:16:03'
    @staticmethod
    def get_current_date_and_time_in_different_format(self):
        try:
            current_date_time = datetime.now()
            current_date_time_format = current_date_time.strftime("%B %d,%Y %H:%M:%S")
            logging.info("get current date and time in different format e.g. 'August 09,2019 12:16:03'")
            return current_date_time_format           
        except:
            logging.error("current date and time not present in different format")
    
    