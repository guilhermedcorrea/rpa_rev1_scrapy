from dotenv import load_dotenv
from os import path
import os
import time
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import scrapy
from scrapy_splash import SplashRequest 


try:
    import sys
    sys.path.append(r'D:\rpa_rev_01\app\app')
    
except ModuleNotFoundError:
    ...
from base import SeleniumBaseClass


load_dotenv()

SCRAPEOPS_API_KEY = os.getenv('SCRAPEOPS_API_KEY')
anticaptcha = os.getenv('anticaptchatoken')


class SpiderAllowCaptcha(scrapy.Spider):
    
    name = "patrickhlauke"
    allowed_domains = ["patrickhlauke.github.io"]
    start_urls = ["https://patrickhlauke.github.io/recaptcha/"]
    
    custom_settings = {
        'SCRAPEOPS_API_KEY': SCRAPEOPS_API_KEY,
        'SCRAPEOPS_FAKE_HEADERS_ENABLED': True,
        'DOWNLOADER_MIDDLEWARES': {
            'app.middlewares.ScrapeOpsFakeBrowserHeadersMiddleware': 400,
        }
    }
    
    
    def get_selenium_driver(self,url) -> None:
        SeleniumBaseClass().get_selenium_driver(url)
        time.sleep(3)
        
   
        
spider = SpiderAllowCaptcha()
spider.get_selenium_driver('https://patrickhlauke.github.io/recaptcha/')



print(anticaptcha)