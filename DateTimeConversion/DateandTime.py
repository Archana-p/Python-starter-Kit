import time
from datetime import datetime
class DateAndTime():
    
    def getcurrentTimeinMillis(self):
        current_milli_time = lambda: int(round(time.time()* 1000))
        return current_milli_time
    
    def getcurrentDateandTime(self):
        current_date_time = datetime.now()
        current_date_time_format = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
        return current_date_time_format
    
    def getcurrentDateandTimeinDifferentFormat(self):
        current_date_time = datetime.now()
        current_date_time_format = current_date_time.strftime("%B %d,%Y %H:%M:%S")
        return current_date_time_format