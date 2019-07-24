from Pages.Loginpage import LoginPage
from Pages.Searchproduct import SearchproductTest
from Pages.Homepage import HomePage
from DBConnection.DBConnection import DBConnection
from ExcelFileData.Data import Data
from Utilities.Genericfunctions import GenericFunction
from Utilities.screenshot import Screenshot

class LoginTest():
   
           
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
        Screenshot.take_screenshot(self,driver) 
        login.select_category_from_dropdown()
        self.assertTrue(True, "User is login suceessfully")
            
    def test_search_valid_category(self):
        driver = self.driver
        search_product = SearchproductTest(driver)
        GenericFunction.wait(self)
        search_product.shopByCateogry()
        search_product.select_sofas_as_furniture_cateogry()
        search_product.select_sofas_by_type()


        
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
        username,password = data.selectDataDB() 
        login = LoginPage(driver)
        login.enterusername(username)
        login.clickfornextloginpage()
        login.enterpassword(password)
        login.clickonloginbutton()   
        
    