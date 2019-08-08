from Pages.Loginpage import LoginPage
from Pages.Searchproduct import SearchproductTest
from Pages.Homepage import HomePage
from Utilities.Genericfunctions import GenericFunction
from ExcelFileData.Data import Data
from DBConnection.DBConnection import DBConnection
from Config import config


class LoginTest:  
    #login to the Amazon         
    def test_login_valid(self):   
        driver = self.driver 
        #creation object  for loginpage
        login = LoginPage(driver)
        #create object for Data class
        data = Data()
        #navigate to login page
        login.Gotologinpage()
        #enter username for login
        login.enterusername(data.fetch_username())
        #press continue button for entering password
        login.clickfornextloginpage()
        #enter password
        login.enterpassword(data.fetch_password())
        #click on sign in button
        login.clickonloginbutton()
        #image_name = DateAndTime.get_current_date_and_time_in_different_format(self)
        #image_name_into_string = Utilites.convert_to_string(self, image_name)
        driver.save_screenshot(config.IMAGE_PATH+'/login_page.png') 
        login.select_category_from_dropdown()
        self.assertTrue(True, "User is login sucessfully")
      
    #Search for valid product category       
    def test_search_valid_category(self):
        driver = self.driver
        search_product = SearchproductTest(driver)
        GenericFunction.wait(self)
        search_product.shopByCateogry()
        search_product.select_sofas_as_furniture_cateogry()
        search_product.select_sofas_by_type()
     
    #logout from Amazon   
    def test_valid_logout(self):
        driver = self.driver
        GenericFunction.wait(self)
        homepage = HomePage(driver)
        homepage.checkOrders()
        homepage.navigatebacktoHomepage()
        GenericFunction.wait(self)
        homepage.signoutfrompage()  
        #now login by using fetching data from DB
        data = DBConnection()
        username,password = data.select_data_db() 
        login = LoginPage(driver)
        login.enterusername(username)
        login.clickfornextloginpage()
        login.enterpassword(password)
        login.clickonloginbutton()   
        
    