from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

browser=None

#add a command line option of '--browser name_of_browser'
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action='store', default='chrome'
    )

@pytest.fixture(scope='class')
def setup(request):
    global browser
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


#capture the screenshot whenever the test fails
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    browser.get_screenshot_as_file(name)