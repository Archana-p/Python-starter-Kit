import pandas
from pandas import DataFrame
from Utilities.Log import Log

class ExcelHandler:
    
    #this function will read data from excel file
    #excle_file_path is path of file and it will be string and sheet name is also in string format
    #input:data_frame = pandas.read_excel('C:/Users/archanap/Documents/Practice Team work/sample.xlsx',sheet_name='Sheet1')
    #output of data_frame will be 
    #        Number   Name
    # 0       1   john
    # 1       2  Maddy
    #methods are available which can be used  on data frame as per the requirements
    def read_data_from_excel_file(self,excle_file_path,sheet_name):
        try:
            data_frame = pandas.read_excel(excle_file_path,sheet_name=sheet_name)
            return data_frame
            Log.write_info_to_log_file(self,"Data read successfully from excel file")  
        except FileNotFoundError:
            Log.write_errors_to_log_file(self,"File Not Found") 
            
    #***********************************************************************************************#
    #this function will read certain columns data from excel file
    #input:columns=[] array will contain  the name of columns
    #input:excel_file_path is path of file and sheet name is name of sheet will we want to read and both will be in string format
    #input:e.g. data_frame= pandas.read_excel('C:/Users/archanap/Documents/Practice Team work/sample.xlsx',sheet_name='Sheet1',usecols=['Name'])
    #output of data_frame will be 
    #       Name
    #    0   john
    #   1    Maddy
    #methods are available which can be used  on data frame as per the requirements
    def read_certain_columns_from_excel_file(self,excle_file_path,sheet_name,columns=[]):
        
        #columns array contains the name of the columns which need to read from excel File
        try:
            data_frame= pandas.read_excel(excle_file_path,sheet_name= sheet_name,usecols=columns)
            return data_frame.head()
            Log.write_info_to_log_file(self,"specific rows read successfully from excel file")
        except FileNotFoundError:
            Log.write_errors_to_log_file(self,"File not found")
            
    #***********************************************************************************************#
    def write_data_to_excle_file(self,excle_file_path,excle_file_data,excle_file_column=[],excle_file_sheet_name):
        #example for excel file data
        #input:excel_file_data = pandas.DataFrame({'Number':[3,4],
        #                                   'Name':['Joy','Joe']})
        #input:data_frame = DataFrame(excel_file_data,columns=['Number','Name'])
        #input:data_frame =data_frame.to_excel('C:/Users/archanap/Documents/Practice Team work/sample.xlsx','Sample',index = False)
        #Output:Open the file and check data will be entered in file make sure while doing writing operation file will be closed or else permission denied error will occured
        #methods are available which can be used  on data frame as per the requirements
        try:
            data_frame = DataFrame(excle_file_data, columns= excle_file_column)
            data_frame= data_frame.to_excle (excle_file_path, sheet_name = excle_file_sheet_name,index = False)
            return data_frame
            Log.write_info_to_log_file(self,"Data written successfully in excel file")
        except IOError:
            Log.write_errors_to_log_file(self,"Data writing failed in excel file")
