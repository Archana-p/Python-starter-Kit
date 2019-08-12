from Pages.Loginpage import LoginPage
from Pages.Searchproduct import SearchproductTest
from Pages.Homepage import HomePage
from Utilities.WebActions import WebActions
from ExcelFileData.Data import Data
from Utilities.screenshot import screenshot


class LoginTest:  
    #this test case perform login functionality on amazon page        
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
        #driver.save_screenshot(config.IMAGE_PATH+'/login_page.png') 
        screenshot.capture_screenshot(self)
        login.select_category_from_dropdown()
        self.assertTrue(True, "User is login sucessfully")
      
    #this test case will Search for valid product category       
    def test_search_valid_category(self):
        driver = self.driver
        search_product = SearchproductTest(driver)
        WebActions.wait(self)
        search_product.shopByCateogry()
        search_product.select_sofas_as_furniture_cateogry()
        search_product.select_sofas_by_type()
     
    #this test case perform log out functionality on Amazon page   
    def test_valid_logout(self):
        driver = self.driver
        WebActions.wait(self)
        homepage = HomePage(driver)
        homepage.checkOrders()
        homepage.navigatebacktoHomepage()
        WebActions.wait(self)
        homepage.signoutfrompage()  
        #now login by using fetching data from DB
        #data = DBConnection()
        #username,password = data.select_data_db() 
        #login = LoginPage(driver)
        #login.enterusername(username)
        #login.clickfornextloginpage()
        #login.enterpassword(password)
        #login.clickonloginbutton()   
        
    