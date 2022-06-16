from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture(scope='class')
def setup():
    browser = webdriver.Chrome(service=Service("C:\\Users\\sande\\Desktop\\Programs\\chromedriver.exe"))
    browser.get('https://rahulshettyacademy.com/angularpractice/')
    browser.maximize_window()

