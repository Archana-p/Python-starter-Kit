import mysql.connector
from Utilities.Log import Log
from selenium.common.exceptions import TimeoutException
from Config import DBDetails

mydb=mysql.connector.connect(
                            host = DBDetails.HOST,
                            user =DBDetails.USERNAME,
                            password =DBDetails.PASSWORD,
                            database = DBDetails.DBNAME
                          )

cursor = mydb.cursor()

class MySql:
    
    #this function will create  ,drop table for user
    #input will be sql query for creation of table
    #e.g query = """CREATE TABLE EMPLOYEE (
    #    FIRST_NAME  CHAR(20) NOT NULL,
    #     LAST_NAME  CHAR(20),
    #     AGE INT,  
    #     SEX CHAR(1),
    #     INCOME FLOAT )"""
    #input will be sql query for dropping table
    #cursor.execute("DROP TABLE IF EXISTS EMPLOYEE"     
    
    def execute_query_on_table(self,query,msg):
        try:
            cursor.execute(query)
            Log.write_info_to_log_file(self,msg)
        except TimeoutException:
            Log.write_errors_to_log_file(self, msg)
            
        #disconnect from server   
        mydb.close()   
               
    #*************************************************************************************************************#
    #this function will insert ,delete and updated the record in db 
    #input will be sql query for insert records
    ## Prepare SQL query to INSERT a record into the database.
    #query = "INSERT INTO EMPLOYEE(FIRST_NAME, \
    #   LAST_NAME, AGE, SEX, INCOME) \
    #   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
    #   ('Mac', 'Mohan', 20, 'M', 2000)
    #***********************************************************************************#
    ## Prepare SQL query to UPDATE required records
    #query = "UPDATE EMPLOYEE SET AGE = AGE + 1
    #                     WHERE SEX = '%c'" % ('M')
    #query = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)   
    def execute_query_on_records_from_DB(self,query,msg):
        try:
            #Execute the SQL command
            cursor.execute(query)
            Log.write_info_to_log_file(self,msg)
            mydb.commit()
        except TimeoutException:
            #rollback in case there is any error
            mydb.rollback()
            Log.write_errors_to_log_file(self, msg)  
            
        mydb.close()
        
    #*************************************************************************************************************#
    #In case the number of rows in the table is small, you can use the  fetchall() method to fetch all rows from the database table
    #input will be query = "select * from books"
    #output will be array of rows
    def fetch_all_rows(self,query):
        try:
            cursor.execute(query) 
            rows = cursor.fetchall()
            total_row_count = cursor.rowcount
            Log.write_info_to_log_file(self, "Fetch all rows from tabel and rows count will be :"+total_row_count)
            return rows 
        except TimeoutException:
            Log.write_errors_to_log_file(self, "Error occurred while fetching records from table")
            
        mydb.close()
    #*************************************************************************************************************#
    #The  fetchone() method returns the next row of a query result set or None in case there is no row left. 
    #Input will be query ="select * from books"
    #output will be single row written
    def query_with_fetchone(self,query):
        try:
            cursor.execute(query)
            row = cursor.fetchone()
            Log.write_info_to_log_file(self, "Fetch next row from query result set or None in case there is no row left")
            return row
        except TimeoutException:
            Log.write_errors_to_log_file(self, "Error occurred while fetching records by using fetchone() method")
        mydb.close()
    