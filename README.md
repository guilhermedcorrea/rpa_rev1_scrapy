
#Iniciando o projeto - SCRAPY

pip install -r requirements.txt


#https://docs.scrapy.org/en/latest/index.html

#CADASTRAR https://scrapeops.io/app/dashboard



-Cria um produto Spider

#scrapy startproject tutorial


-leva ate a pasta onde fica os spiders
cd rpajob

-cria um novo codigo base
scrapy genspider example example.com




```Python

    
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

```
<b>Classe Selenium Base- Todos os Spiders criados herdam os metodos dele. No mesmo Arquivo Base tem classes PyautoGuiBase, SeleniumActionsChainBase, OpencvBase</b>

<b>Proxy scrapeops</b>


```Python

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


```
<b>Proxy</b>



```Python

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


```
<b>FakeUser Agente</b>


```Python

"""Fake User Agent"""
class ScrapeOpsFakeUserAgentMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def __init__(self, settings) -> Any:
        self.scrapeops_api_key = settings.get('SCRAPEOPS_API_KEY')
        self.scrapeops_endpoint = settings.get('SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT', 'http://headers.scrapeops.io/v1/user-agents?') 
        self.scrapeops_fake_user_agents_active = settings.get('SCRAPEOPS_FAKE_USER_AGENT_ENABLED', False)
        self.scrapeops_num_results = settings.get('SCRAPEOPS_NUM_RESULTS')
        self.headers_list = []
        self._get_user_agents_list()
        self._scrapeops_fake_user_agents_enabled()

    def _get_user_agents_list(self):
        payload = {'api_key': self.scrapeops_api_key}
        if self.scrapeops_num_results is not None:
            payload['num_results'] = self.scrapeops_num_results
        response = requests.get(self.scrapeops_endpoint, params=urlencode(payload))
        json_response = response.json()
        self.user_agents_list = json_response.get('result', [])

    def _get_random_user_agent(self):
        random_index = randint(0, len(self.user_agents_list) - 1)
        return self.user_agents_list[random_index]

    def _scrapeops_fake_user_agents_enabled(self):
        if self.scrapeops_api_key is None or self.scrapeops_api_key == '' or self.scrapeops_fake_user_agents_active == False:
            self.scrapeops_fake_user_agents_active = False
        self.scrapeops_fake_user_agents_active = True
    
    def process_request(self, request, spider):        
        random_user_agent = self._get_random_user_agent()
        request.headers['User-Agent'] = random_user_agent



```
<b>Middlewares- Tem todas as classes responsaveis pelo controle da aplicação em si e suas integrações</b>




```Python

DOWNLOADER_MIDDLEWARES = {
    'app.middlewares.ScrapeOpsFakeBrowserHeadersMiddleware': 400,
}


DOWNLOADER_MIDDLEWARES = {
    'app.SeleniumMiddleware': 800
}


DOWNLOADER_MIDDLEWARES = {
    'app.SplashCookiesMiddleware': 723,
    'app.SplashMiddleware': 725,
    'app.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Enable Splash Deduplicate Args Filter
SPIDER_MIDDLEWARES = {
    'app.SplashDeduplicateArgsMiddleware': 100,
}

# Define the Splash DupeFilter
DUPEFILTER_CLASS = 'app.SplashAwareDupeFilter'



# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "app.middlewares.AppSpiderMiddleware": 543,
#}


```


<b>Importações externas</b>



```Python

schedulers = Table(
    "schedulers",
    metadata_obj,
    Column("cod_scheduler", Integer, primary_key=True),
    Column("data", datetime, nullable=False),
    Column("dia", Integer),
    Column("mes", Integer, nullable=False),
    Column("status", String(50), nullable=False),
    Column("falha", String(50), nullable=False),
    Column("tempo", Integer, nullable=False),
    Column("funcaopython", String(50), nullable=False),
    schema="RPA"
)

usuarioRpa = Table(
    "usuario_rpa",
    metadata_obj,
    Column("cod_usuario", Integer, primary_key=True),
    Column("nome", String(16), nullable=False),
    Column("email", String(60)),
    Column("data_cadastro", datetime, nullable=False),
    Column("data_atualizacao", datetime, nullable=False),
    Column("cod_scheduler", Integer, ForeignKey("schedulers.cod_scheduler")),
    schema="RPA"
)

```

<b>Modelos Tabelas</b>



```Python

class SchedulerTask:
    def __init__(self):
        ...
        
        

jobstores = {
    'mongo': {'type': 'sqlalchemy'},
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': {'type': 'threadpool', 'max_workers': 20},
    'processpool': ProcessPoolExecutor(max_workers=5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler()


scheduler.configure(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)


```

<b>Schedulers das tasks</b>