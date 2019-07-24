from Config import config
from Screenshot import Screenshot_Clipping
from DateTimeConversion.DateandTime import DateAndTime
class Screenshot():
    
    def take_screenshot(self, driver):
        driver = self.driver
        image_path = config.IMAGE_PATH
        ob=Screenshot_Clipping.Screenshot()
        image_name = DateAndTime.getcurrentDateandTimeinDifferentFormat(self)
        ob.full_Screenshot(driver, save_path=image_path, image_name=image_name+'.png')
