import logging 
from Config  import config



logging.basicConfig(filename= config.LOG_FILE_PATH,filemode='w')


class Log:
    
    #this function will write the errors to log file
    def write_errors_to_log_file(self,msg): 
        logger_error = logging.getLogger()               
        logger_error.setLevel(logging.ERROR)
        logger_error.error(msg)
    
    #this function will write the info message to log file
    def write_info_to_log_file(self,msg):
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info(msg)
        