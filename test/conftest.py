from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

#add a command line option of '--browser name_of_browser'
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action='store', default='chrome'
    )

@pytest.fixture(scope='class')
def setup(request):
    #this is how we can get the value of '--browser' key
    browser_name = request.config.getoption("browser")
    
    if browser_name == "chrome":
        browser = webdriver.Chrome(service=Service("C:\\Users\\sande\\Desktop\\Programs\\chromedriver.exe"))
    elif browser_name == "firefox":
        browser = webdriver.Firefox(service=Service("C:\\Users\\sande\\Desktop\\Programs\\geckodriver.exe"))
    elif browser_name == 'edge':
        browser = webdriver.Edge(service=Service("C:\\Users\\sande\\Desktop\\Programs\\msedgedriver.exe"))
    
    browser.get('https://rahulshettyacademy.com/angularpractice/')
    browser.maximize_window()

    #whichever class request browser pass this browser
    request.cls.browser = browser
    yield
    browser.close()