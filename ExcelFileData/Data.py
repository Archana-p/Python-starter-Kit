import xlrd

loc =("C:/Users/archanap/Documents/Practice Team work/data.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)


class Data():
                
    def fetch_username(self):
        username_value = sheet.row_slice(rowx=1,start_colx=0,end_colx=1)
        return username_value[0].value
        
    
    def fetch_password(self):
        password_value = sheet.row_slice(rowx=1,start_colx=1,end_colx=2)
        return password_value[0].value
        
