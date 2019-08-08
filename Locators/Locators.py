class Locators:
    
    #homepage objects 
    Nav_order_page_class_name = "nav-orders"
    Nav_home_page_class_name="nav-logo-link"
    Logout_id = "//*[@id='nav-item-signout']"
    Logout_Link_Text = "Sign Out"
    logout_css_selector="#nav-item-signout"
    
    #login page Object 
    SignIn_Button_id = "nav-link-accountList"
    Username_TextBox_id = "ap_email"
    Continue_Button_id ="continue"
    Password_TextBox_id ="ap_password"
    Login_button_id ="signInSubmit"
    select_dropdown_option_id = "searchDropdownBox"
    search_text_box_id = "twotabsearchtextbox"
    
    #shop by category filters 
    shop_all_product_list_id ="nav-link-shopall"
    select_kitche_tool_category_label ="//*[@id='nav-flyout-shopAll']/div[2]/span[10]/span"
    select_furniture_category_by_xpath = "//*[@id='nav-flyout-shopAll']/div[3]/div[10]/div[1]/div/a[3]"
    select_sofas_as_furniture_category_by_xpath = "//div[@class='left_nav browseBox']//ul[1]/li[1]/a[contains(text(),'Sofas & Couches')]"
    select_sofa_type_by_xpath = "//div[@id='leftNav']/ul[5]//input[@type='checkbox']"