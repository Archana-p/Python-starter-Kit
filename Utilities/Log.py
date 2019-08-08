import logging 


class Log:
    
    #this function will write the errors to log file
    def write_errors_to_log_file(self,msg):
        LOG_FILENAME ='C:/Users/archanap/Documents/Practice Team work/Python POC/POC_updated/Logs/errors.log'
        logging.basicConfig(filename=LOG_FILENAME ,level=logging.error)
        logging.error(msg)
    
    #this function will write the info message to log file
    def write_info_to_log_file(self,msg):
        LOG_FILENAME = 'info.log'
        logging.basicConfig(filename=LOG_FILENAME,level=logging.info)
        logging.info(msg)