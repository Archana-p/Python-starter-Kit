import sqlite3
conn = sqlite3.connect('test.db')
class DBConnection():
          
    def createDB(self):
        #creation of table
        conn.execute('''CREATE TABLE PERSON
                   (ID INT PRIMARY KEY,
                    USERNAME TEXT,
        PASSWORD PASSWORD);''')
        print("Table created")
     
    def InsertRecordinDB(self):
        #insert records in table
        conn.execute("INSERT INTO  PERSON(ID ,USERNAME,PASSWORD)VALUES(1,'pythonuser@gmail.com','password@123')")
        conn.commit()
        print("Record inserted successfully") 
    
    def selectDataDB(self):
        data = conn.execute("SELECT ID,USERNAME,PASSWORD FROM PERSON")
        for row in data:
            username = row[1]
            password = row[2]
            return username ,password
        print("data display successfully")        

    def closeConnetion(self):
        conn.close()