import urllib3
import logging
import traceback


class URLNavigationException:
    
    #this function handles the url navigation exceptions.
    def handle_url_navigation_exception(self,url):
        http = urllib3.PoolManager()
        
        try:
            http.request('GET',url)
        except urllib3.exceptions.ConnectTimeoutError:
            logging.error("Socket timeout occurs while connecting to server")
        except urllib3.exceptions.HTTPError:
            logging.error("Automatic decoding  based on Content-Type fails")
        except urllib3.exceptions.NewConnectionError:
            logging.error("Failed to establish new connection")
        except urllib3.exceptions.ReadTimeoutError:
            logging.error("Socket timeout occurs while receiving data from server")
        except urllib3.exceptions.SSLError:
            logging.error("SSL certificate fails in an HTTPS connection")
        except urllib3.exceptions.HTTPWarning:
            logging.error("Base Warning used by this module")
        except urllib3.exceptions:
            logging.error('generic Exception:'+traceback.format_exc())