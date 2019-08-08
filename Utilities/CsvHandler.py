import pandas
from pandas import DataFrame
import logging


class CsvHandler:
 
    def read_data_from_csv_file(self,csv_file_path):
        try:
            #csv_file_path = file location will be given 
            #it will read all the data from csv file stroed in data variable
            data = pandas.read_csv(csv_file_path, index_col=0)
            return data.head()
            logging.info("Data read successfully from file")
        except FileNotFoundError:
            logging.error("Data reading from csv file failed")
     
    def write_data_to_csv_file(self,csv_file_data,csv_file_name,csv_file_columns =[]):  
        # example for csv_file_data 
        #C = {'Programming language': ['Python','Java', 'C++'],
        #'Designed by': ['Guido van Rossum', 'James Gosling', 'Bjarne Stroustrup'],
        #'Appeared': ['1991', '1995', '1985'],
        #'Extension': ['.py', '.java', '.cpp'],
        #csv_file_columns = ['Programming language', 'Designed by', 'Appeared', 'Extension']
        #} then code will be df = DataFrame(C, columns=csv_file_columns )
        #X:\pandaresult.csv is csv file name 
        #export_csv = df.to_csv (r'X:\pandaresult.csv', index = None, header=True) 
        try:
            data_frame = DataFrame(csv_file_data, columns= csv_file_columns)
            data_frame= data_frame.to_csv (r'csv_file_name', index = None, header=True) 
            # here you have to write path, where result file will be stored
            return data_frame
            logging.info("data written successfully on csv file")
        except IOError:
            logging.error("Data writing failed")
            
    def read_csv_file_from_harddrive(self,csv_file_name):
        try:
            #csv_file_name = file name like abc.csv 
            #it will read all the data from csv file stroed in data variable
            data = pandas.read_csv(csv_file_name)
            return data.head()
        except FileNotFoundError:
            logging.error("Data reading from csv file failed")
    
    def read_certain_columns_from_csv_file(self,csv_file_path,colums=[]):
        try:
            #columns = ['name','id'] pass an index of columns that you want to read
            data_frame = pandas.read_csv(csv_file_path,index_col=0,usecols=colums)
            return data_frame.head()
            logging.info("specific columns read from csv file")
        except FileNotFoundError:
            logging.error("File not found")
    
    def read_certain_rows_from_csv_file(self,csv_file_path,number_of_rows):
        try:
            #number_of_rows value is 8 then it will return first 8 rows from cvs file
            data_frame =pandas.read_csv(csv_file_path,nrows=number_of_rows)
            return data_frame
            logging.info("specific rows read from csv file")
        except FileNotFoundError:
            logging.error("File not Found")