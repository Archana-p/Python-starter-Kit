from Config import config
from Screenshot import Screenshot_Clipping
from DateTimeConversion.DateAndTime import DateAndTime
from selenium.common.exceptions import TimeoutException
from Utilities.utilities import Utilites
from Utilities.Log import Log


class Screenshot:
    
    def take_screenshot(self, driver):
        try:
            driver = self.driver
            image_path = config.IMAGE_PATH
            ob=Screenshot_Clipping.Screenshot()
            image_name = DateAndTime.get_current_date_and_time(self)
            image_name = Utilites.convert_to_string(self, image_name)
            ob.full_Screenshot(driver, save_path=image_path, image_name= image_name+'.png')
            Log.write_info_to_log_file(self,"screenshot taken successfully")
        except TimeoutException:
            Log.write_errors_to_log_file(self, "screenshot is not taken properly")
