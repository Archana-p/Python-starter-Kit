from Config import Driver ,config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class BrowserType:
    
    
    #this function will setup the path for chrome browser
    def setup_chrome_webdriver(self):
        self.driver = webdriver.Chrome(executable_path= Driver.CHROME_DRIVER_PATH)
        return self.driver
    
    #this function will setup the path for IE browser
    def setup_IE_webdriver(self):
        #path = os.path.join(path, 'x86', 'IEDriverServer.exe')
        cap = DesiredCapabilities().INTERNETEXPLORER
        cap['platform'] = "windows"
        cap['version'] = "11"
        cap['browserName'] = "internet explorer"
        cap['ignoreProtectedModeSettings'] = True
        cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
        cap['nativeEvents'] = True
        cap['ignoreZoomSetting'] = True
        cap['requireWindowFocus'] = True
        cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
        self.driver = webdriver.Ie(executable_path=Driver.IE_DRIVER_PATH,desired_capabilities=cap)
        return self.driver
    
    #this function will setup the path for FireFox browser
    def setup_firefox_webdriver(self):
        self.driver = webdriver.Firefox(executable_path=Driver.FIREFOX_DIRVER_PATH)
        return self.driver
        
    #this function will run test case in different browser browser_type is argument where we can pass type of browser we want   
    def get_browser_value(self,browser_type):      
        if browser_type == 'Chrome':
            self.driver = BrowserType.setup_chrome_webdriver(self)
            self.driver.get(config.APPLICATION_URL)
            #return self.driver
        elif browser_type == 'IE':
            self.driver = BrowserType.setup_IE_webdriver(self)
            self.driver.get(config.APPLICATION_URL)
            #return self.driver
        elif browser_type == 'FireFox':
            self.driver = BrowserType.setup_firefox_webdriver(self)
            self.driver.get(config.APPLICATION_URL)
            #return self.driver
        else:
            print("Invalid Value")       
            