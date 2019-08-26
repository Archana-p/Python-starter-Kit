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
        #system.setProperty("webdriver.ie.driver",Driver.IE_DRIVER_PATH)
        self.driver = webdriver.Ie(executable_path= r'../Python POC/POC_updated/Drivers/IEDriverServer_x64_3.141.59/IEDriverServer.exe',desired_capabilities=cap)
        #self.driver = webdriver.Remote(command_executor='http://127.0.0.1:5555',
        # desired_capabilities=cap)
        return self.driver
    
    #this function will setup the path for FireFox browser
    def setup_firefox_webdriver(self):
        self.driver = webdriver.Firefox(executable_path=Driver.FIREFOX_DIRVER_PATH)
        return self.driver
        
    #this funcation will take browser type as value and initiated the browser 
    #browser type value will be 'Chrome','IE','FireFox'
    def get_browser_value(self,browser_type):      
        if browser_type == 'Chrome':
            self.driver = BrowserType.setup_chrome_webdriver(self)
            self.driver.get(config.APPLICATION_URL)
        elif browser_type == 'IE':
            self.driver = BrowserType.setup_IE_webdriver(self)
            self.driver.get(config.APPLICATION_URL)
        elif browser_type == 'FireFox':
            self.driver = BrowserType.setup_firefox_webdriver(self)
            self.driver.get(config.APPLICATION_URL)
        else:
            print("Invalid Value")       
            