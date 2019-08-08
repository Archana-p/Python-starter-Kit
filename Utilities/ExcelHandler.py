import pandas
from pandas import DataFrame
import logging

class ExcelHandler:
    
    
    def read_data_from_excel_file(self,excle_file_name,sheet_name):
        #excel_file_name = name of the  file 
        #sheet_name = excel file sheet name
        try:
            data_frame = pandas.read_excel(excle_file_name,sheet_name=sheet_name)
            return data_frame.head() 
            logging.info("Data read successfully from excel file")  
        except FileNotFoundError:
            logging.error("File Not Found") 
            
    
    def read_certain_columns_from_excel_file(self,excle_file_name,sheet_name,columns=[]):
        
        #columns array contains the name of the columns which need to read from excel File
        try:
            data_frame= pandas.read_excel(excle_file_name,sheet_name= sheet_name,usecols=columns)
            return data_frame.head()
            logging.info("specific rows read successfully from excle file")
        except FileNotFoundError:
            logging.error("File not found")
            
    
    def write_data_to_excle_file(self,excle_file_name,excle_file_data,excle_file_column=[],excle_file_sheet_name):
        #example for excle file data
        #df = pd.DataFrame({'Names':['Andreas', 'George', 'Steve',
        #                   'Sarah', 'Joanna', 'Hanna'],
        #         'Age':[21, 22, 20, 19, 18, 23]})
        try:
            data_frame = DataFrame(excle_file_data, columns= excle_file_column)
            data_frame= data_frame.to_excle (excle_file_name, sheet_name = excle_file_sheet_name,index = False)
            return data_frame
            logging.info("Data written successfully in excle file")
        except IOError:
            logging.error("Data writing failed in excle file")
