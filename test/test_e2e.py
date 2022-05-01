from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        # we defined browser opening inside the 'setup method' in 'conftest.py'
        #  file we will use it with the help of fixture.

        wait = WebDriverWait(self.browser, 10)

        #click shop button
        self.browser.find_element(By.CSS_SELECTOR, "a[href*=shop]").click()

        #getting all the products in page
        products = self.browser.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in products:
            if product.find_element(By.XPATH, "div/h4/a").text == 'Blackberry':
                product.find_element(By.XPATH, "div/button").click()

        #checkout button
        self.browser.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.browser.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()

        #input box - entering "ind"
        self.browser.find_element(By.CSS_SELECTOR, "#country").send_keys('ind')

        #wait till the link text India is present and then click on it
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.browser.find_element(By.LINK_TEXT, "India").click()

        #click on t&c checkbox and then on purchase button
        self.browser.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        #get the success msg printed on webpage verify it if it's matching
        success_text = self.browser.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in success_text

        #taking a screenshot of the page
        self.browser.get_screenshot_as_file('ss.png')