import mss
import mss.tools
from Utilities.Log import Log


class screenshot:
    #this function will capture the full screen screenshot just called this function where needed
    def capture_screenshot(self):
        with mss.mss() as sct:
            # The screen part to capture           
            monitor = {"top": 160, "left": 160, "width": 160, "height": 135}            
            output = "C:/Users/archanap/Documents/Practice Team work/Python POC/POC_updated/Images/sct-{top}x{left}_{width}x{height}.png".format(**monitor)        
            filename = sct.shot(mon=-1, output=output)
            Log.write_info_to_log_file(self, filename)