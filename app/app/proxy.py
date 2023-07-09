import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
from os import path
import os

load_dotenv()


SCRAPEOPS_API_KEY = os.getenv('SCRAPEOPS_API_KEY')
print(SCRAPEOPS_API_KEY)



proxy_params = {
      'api_key': SCRAPEOPS_API_KEY,
      'url': 'http://httpbin.org/ip', 
  }

response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params=urlencode(proxy_params),
  timeout=120,
)

print('Body: ', response.content)



