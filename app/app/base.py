from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from typing import Any,Dict
import pyautogui
import cv2
from abc import ABC, abstractmethod
import time
from dataclasses import dataclass
import os
import scrapy

from scrapy import Request
from scrapy.crawler import Crawler

from scrapy_selenium.http import SeleniumRequest
from scrapy_selenium.middlewares import SeleniumMiddleware

class PyAutoGuiClass:
    ...


@dataclass
class OpenCvClass:
    name: str
    path: str
    
    def image_reader(self, path, name):
        os.path.join(path,name)
        

@dataclass
class SaveItems:
    name: str
    path: str
    data: datetime
    
    def save_item(self, path, name):
        os.path.join(path,name)
        self.data
        
    
"""Classe Base Interação Database 'Sql server'"""
class SqlServerClass:
    ...

"""Classe Base Selenium ActionsChains"""
class SeleniumActionsChains:
    ...
    
    
"""Classe Base Selenium"""
class SeleniumBaseClass:
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--start-maximized")
    options.add_argument('--disable-infobars')
    prefs ={"download.default_directory":r"D:\rpa_rev_01\files"}
    options.add_experimental_option("prefs",prefs)
    
    service = Service(executable_path=r'D:\rpa_rev_01\chromedriver\chromedriver.exe')
    driver = webdriver.Chrome(options=options,service=service)
    
    data_atual = str(datetime.today().strftime('%Y-%m-%d %H:%M'))
    
    def implicity_way(self, time) -> None:
        self.driver.implicitly_wait(time)
    
    def get_selenium_driver(self,url) -> None:
        self.implicity_way(20)
        print(url)
        self.driver.get(url)
        time.sleep(10)
      
        
    def scroll_infinit_page(self) -> None:
        
        self.implicity_way(20)
        
        lenOfPage = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True
       
    def find(self,*args, **kwargs):
        ...
        
    def find_note(self,*args, **kwargs):
        ...
    
    def check_handlers(self, *args, **kwargs):
        ...
        
    def find_iframe(self,*args, **kwargs):
        ...