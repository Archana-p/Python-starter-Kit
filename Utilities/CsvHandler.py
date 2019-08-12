import pandas
from pandas import DataFrame
from Utilities.Log import Log


class CsvHandler:
    #Input : csv_file_path = file location will be given and it will be string 
    #e.g file has two column number and name so output will be in tabular format
    #function call : data = pandas.read_csv('C:/Users/archanap/Documents/Practice Team work/sample.csv',index_col=0)
    #Output will be in table format
    #number Name 
    #1       Abc
    #2       Xyz
    #3       qwe
    #it will read all the data from csv file stored in data variable
    def read_data_from_csv_file(self,csv_file_path):
        try:
            
            data = pandas.read_csv(csv_file_path, index_col=0)
            Log.write_info_to_log_file(self,"Data read successfully from file")
            return data
        except FileNotFoundError:
            Log.write_errors_to_log_file(self,"Data reading from csv file failed")
    
    #*****************************************************************************************#
    # example for csv_file_data 
        #input = csv_file_data = {'Number':[4,5],
        #                'Name':['john','Maddy']}
        #input =csv_file_columns = ['Number','Name']
        #called : data_frame = DataFrame(csv_file_data,columns= csv_file_columns)
        #called :data_frame = data_frame.to_csv('C:/Users/archanap/Documents/Practice Team work/sample.csv',index=None,header=True)
        #output: data will be written in csv file open the file and check the data make sure will running this function csv file will be closed .
    def write_data_to_csv_file(self,csv_file_data,csv_file_name,csv_file_columns =[]):  
        
        try:
            data_frame = DataFrame(csv_file_data, columns= csv_file_columns)
            data_frame= data_frame.to_csv (r'csv_file_name', index = None, header=True) 
            # here you have to write path, where result file will be stored
            Log.write_info_to_log_file(self, "data written successfully on csv file")
            return data_frame
            #open file and data will be present in file
        except IOError:
            Log.write_errors_to_log_file(self,"Data writing failed")
    
    #*****************************************************************************************#
    
    #csv_file_name = file name like 'abc.csv' 
    #it will read all the data from csv file stored in data variable 
    #Input:e.g data = pandas.read_csv('sample.csv')
    #output : Number   Name
    #    0       4   john
    def read_csv_file_from_harddrive(self,csv_file_name):
        try:
            
            data = pandas.read_csv(csv_file_name)
            return data.head()
        except FileNotFoundError:
            Log.write_errors_to_log_file(self,"Data reading from csv file failed")
    
    #*****************************************************************************************#
    #this function is used to read certain columns from csv file
    #input:columns = ['Name'] pass this value for usecols and
    # output will be
    #        Name
    #    0    john
    #    1    Maddy
    def read_certain_columns_from_csv_file(self,csv_file_path,columns=[]):
        try:
            
            data_frame = pandas.read_csv(csv_file_path,usecols=columns)
            Log.write_info_to_log_file(self,"specific columns read from csv file")
            return data_frame.head()           
        except FileNotFoundError:
            Log.write_errors_to_log_file(self,"File not found")
            
    
    #*****************************************************************************************#
    #this function will read data as per the rows count we can provide number of rows we want to read from csv file 
    #input:e.g. data_frame =pandas.read_csv('C:/Users/archanap/Documents/Practice Team work/sample.csv',nrows=1)
    #output of data_frame will be  Number  Name
    #                       0       4  john
    #it will written only one row as i provide row count = 1 
    def read_certain_rows_from_csv_file(self,csv_file_path,number_of_rows):
        try:
            #number_of_rows value is 8 then it will return first 8 rows from cvs file
            data_frame =pandas.read_csv(csv_file_path,nrows=number_of_rows)
            Log.write_info_to_log_file(self,"specific rows read from csv file")
            return data_frame           
        except FileNotFoundError:
            Log.write_errors_to_log_file(self, "File not Found")