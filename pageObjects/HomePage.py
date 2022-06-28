from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage

class HomePage:
    #to receive the driver/browser from the test_e2e.py, we need to define the constructor
    def __init__(self, browser):
        self.browser = browser
        

    #assigning the selector to shop variable for clicking the shop button
    shop = (By.CSS_SELECTOR, "a[href*=shop]")

    #for testTwo or testHomePage.py
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    #to click on the checkbox
    check = (By.ID, "exampleCheck1")  
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMsg = (By.CSS_SELECTOR, "[class*='alert-success']")


    def getShopItems(self):
        #that * tells it to take it as webelement, it deserializes it as tuple
        self.browser.find_element(*HomePage.shop).click()
        #passing the browser/driver to CheckoutPage.py so we don't to pass it from
        # the test_e2e.py file
        checkOutPage = CheckOutPage(self.browser)
        return checkOutPage

    def getName(self):
        return self.browser.find_element(*HomePage.name)

    def getEmail(self):
        return self.browser.find_element(*HomePage.email)

    def getCheck(self):
        return self.browser.find_element(*HomePage.check)

    def getGender(self):
        return self.browser.find_element(*HomePage.gender)

    def getSubmit(self):
        return self.browser.find_element(*HomePage.submit)

    def getSuccessMsg(self):
        return self.browser.find_element(*HomePage.successMsg)