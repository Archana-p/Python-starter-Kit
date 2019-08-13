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
    
    #this function will create table for user
    #input will be sql query for creation of table
    #e.g query = """CREATE TABLE EMPLOYEE (
    #    FIRST_NAME  CHAR(20) NOT NULL,
    #     LAST_NAME  CHAR(20),
    #     AGE INT,  
    #     SEX CHAR(1),
    #     INCOME FLOAT )"""
    def create_table(self,query):
        try:
            cursor.execute(query)
            Log.write_info_to_log_file(self, "Created table successfully")
        except TimeoutException:
            Log.write_errors_to_log_file(self, "Error while creating table")
            
        #disconnect from server
        mydb.close()    
        
    #*************************************************************************************************************#
    #this function will drop the table if it exists
    #input will be sql query for dropping table
    #cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    def drop_table(self,query):
        try:
            cursor.execute(query)
            Log.write_info_to_log_file(self, "Drop table successfully")
        except TimeoutException :
            Log.write_errors_to_log_file(self, "Error while dropping table")
            
        #disconnect from server    
        mydb.close()       
        
    #*************************************************************************************************************#
    #this function will insert the record in db 
    #input will be sql query 
    ## Prepare SQL query to INSERT a record into the database.
    #query = "INSERT INTO EMPLOYEE(FIRST_NAME, \
    #   LAST_NAME, AGE, SEX, INCOME) \
    #   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
    #   ('Mac', 'Mohan', 20, 'M', 2000)
    def insert_record_in_table(self,query):
        try:
            # Execute the SQL command
            cursor.execute(query)
            # Commit your changes in the database
            Log.write_info_to_log_file(self, "Records inserted into database")
            mydb.commit()
        except TimeoutException:
            # Rollback in case there is any error
            mydb.rollback()
            Log.write_errors_to_log_file(self, "Error while inserting records in DB")
            
        #disconnect from server   
        mydb.close()
    #***********************************************************************************#
    #this function will update the records from db
    #input will be sql query 
    ## Prepare SQL query to UPDATE required records
    #query = "UPDATE EMPLOYEE SET AGE = AGE + 1
    #                     WHERE SEX = '%c'" % ('M')
    def update_record_in_table(self,query):
        try:
            #Execute the SQL command
            cursor.execute(query)
            #commit your changes in the database
            Log.write_info_to_log_file(self, "updated record successfully")
            mydb.commit()
        except TimeoutException:
            #rollback in case there is any error
            mydb.rollback()
            Log.write_errors_to_log_file(self, "Error while updating records")
    
        mydb.close()
    
    #*************************************************************************************************************#
    #this function will delete the records from table 
    #input will be sql query
    #query = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
    def delete_record_from_table(self,query):
        try:
            #Execute the SQL command
            cursor.execute(query)
            #commit your changes in the database
            Log.write_info_to_log_file(self, "deleted records successfully")
            mydb.commit()
        except TimeoutException:
            #rollback in case there is any error
            mydb.rollback()
            Log.write_errors_to_log_file(self, "Error occured while deleting record")
    
        mydb.close()
    
    
    #*************************************************************************************************************#
    #this function will select records from table and input will be sql query 
    #query = ("SELECT first_name, last_name, hire_date FROM employees "
    #    "WHERE hire_date BETWEEN %s AND %s")
    def select_record_from_table(self,query):
        try:
            cursor.execute(query)
            Log.write_info_to_log_file(self, "Select records from DB")
            mydb.commit()
        except TimeoutException:
            Log.write_errors_to_log_file(self, "Error occurred while selecting records from DB")
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
    