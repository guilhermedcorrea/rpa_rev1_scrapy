
import requests
from random import randint
import scrapy
from dotenv import load_dotenv
from os import path
import os
from typing import Any

load_dotenv()


from unittest.mock import patch

from scrapy import Request
from scrapy.crawler import Crawler

from scrapy_selenium.http import SeleniumRequest
from scrapy_selenium.middlewares import SeleniumMiddleware

"""Fake user agent"""
SCRAPEOPS_API_KEY = os.getenv('SCRAPEOPS_API_KEY')
print(SCRAPEOPS_API_KEY)


def get_user_agent_list() -> Any:
  response = requests.get('http://headers.scrapeops.io/v1/user-agents?api_key=' + SCRAPEOPS_API_KEY)
  json_response = response.json()
  return json_response.get('result', [])

def get_random_user_agent(user_agent_list) -> Any:
  random_index = randint(0, len(user_agent_list) - 1)
  return user_agent_list[random_index]

'''
## Retrieve User-Agent List From ScrapeOps
#user_agent_list = get_user_agent_list()
'''
url_list = [
  'https://example.com/1',
  'https://example.com/2',
  'https://example.com/3',
  
]



'''
for url in url_list:
    
    ## Add Random User-Agent To Headers
    headers = {'User-Agent': get_random_user_agent(user_agent_list)}

    ## Make Requests
    r = requests.get(url=url, headers=headers)
    print(r.text)
'''