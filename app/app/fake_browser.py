
import requests
from random import randint
from typing import Any
from dotenv import load_dotenv
from os import path
import os

load_dotenv()




SCRAPEOPS_API_KEY = os.getenv('SCRAPEOPS_API_KEY')
print(SCRAPEOPS_API_KEY)


def get_headers_list() -> Any:
  response = requests.get('http://headers.scrapeops.io/v1/browser-headers?api_key=' + SCRAPEOPS_API_KEY)
  json_response = response.json()
  return json_response.get('result', [])

def get_random_header(header_list) -> Any:
  random_index = randint(0, len(header_list) - 1)
  return header_list[random_index]


header_list = get_headers_list()

url_list = [
  'https://example.com/1',
  'https://example.com/2',
  'https://example.com/3',
]

for url in url_list:
  r = requests.get(url=url, headers=get_random_header(header_list))
  print(r.text)
