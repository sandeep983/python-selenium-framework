from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest

#setup method comes from conftest.py
@pytest.mark.usefixtures('setup')
class BaseClass:
    def verifyLinkPresence(self, link_text):
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)