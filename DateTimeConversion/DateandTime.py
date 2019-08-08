import time
import logging
from datetime import datetime
from selenium.common.exceptions import TimeoutException

class DateAndTime:
    
    #this function will convert current time in milli seconds
    @staticmethod
    def get_current_time_in_millis(self):
        try:
            current_milli_time = int(round(time.time()* 1000))
            return current_milli_time
            logging.info("current time converted into millis")
        except TimeoutException:
            logging.error("current time is not converted into millis")
    
    #this function will written current date and time
    @staticmethod
    def get_current_date_and_time(self):
        try:
            current_date_time = datetime.now()
            current_date_time_format = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
            return current_date_time_format
            logging.info("get current Date and Time")
        except TimeoutException:
            logging.error("output for current date and time is not getting")
    
    #this function will written current date and time in different format
    @staticmethod
    def get_current_date_and_time_in_different_format(self):
        try:
            current_date_time = datetime.now()
            current_date_time_format = current_date_time.strftime("%B %d,%Y %H:%M:%S")
            return current_date_time_format
            logging.info("get current date and time in different format")
        except:
            logging.error("current date and time not present in different format")
    
    def get_current_date(self):
        try:
            current_date_time = datetime.now()
            current_date_time_format = current_date_time.strftime("%D%H:%M:%S")
            return current_date_time_format
            logging.info("get current Date and Time")
        except TimeoutException:
            logging.error("output for current date and time is not getting")
