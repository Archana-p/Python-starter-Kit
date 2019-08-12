from selenium.common.exceptions import TimeoutException 
import logging

class comparator:
    
    #This function will compare the two text values and check if they are exactly matching 
    def compare_exact_text(self ,actual_text ,expected_text):
        logging.info("Actual text value ="+actual_text+"Expected text value =" +expected_text)
        try:
            if (actual_text==expected_text):
                logging.info("Text is matched exactly")
                return True
                
        except TimeoutException:
            logging.error("Text are not matching exactly")
    
    #this function will check if two text are partially matched or not
    def compare_partial_text(self,actual_text,expected_text):
        logging.info("Actual text value = "+actual_text+"Expected text value =" +expected_text)
        try:
            if(expected_text in actual_text):
                return actual_text.contains(expected_text)       
        except TimeoutException:
            logging.error("Excepted text is not even partially matching with actual text")