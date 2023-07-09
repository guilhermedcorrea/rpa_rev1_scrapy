from app.app.base import SeleniumBaseClass
import time

class SpiderAllowCaptcha:
    
    def get_selenium_driver(self,url) -> None:
        SeleniumBaseClass().get_selenium_driver(url)
        time.sleep(3)
        
   
        
spider = SpiderAllowCaptcha()
spider.get_selenium_driver('https://patrickhlauke.github.io/recaptcha/')


