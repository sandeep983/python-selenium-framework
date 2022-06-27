from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage

class CheckOutPage:
    #to receive the driver/browser from the test_e2e.py, we need to define the constructor
    def __init__(self, browser):
        self.browser = browser


    #assigning all the titles of the products/cards to cardTitle variable 
    cardTitle = (By.CSS_SELECTOR, ".card-title a")

    #add to cart button
    addToCart = (By.CSS_SELECTOR, ".card-footer button")

    #checkout button
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    #checkout button of next page
    checkoutButtonNext = (By.CSS_SELECTOR, "button[class*='btn-success']")


    def getCardTitles(self):
        #that * tells it to take it as webelement, it deserializes it as tuple
        return self.browser.find_elements(*CheckOutPage.cardTitle)

    def getAddToCart(self):
        return self.browser.find_elements(*CheckOutPage.addToCart)

    def getCheckoutButton(self):
        return self.browser.find_element(*CheckOutPage.checkoutButton)

    def getCheckoutButtonNext(self):
        self.browser.find_element(*CheckOutPage.checkoutButtonNext).click()
        #passing the browser driver to ConfirmPage.py so we don't have to pass it from
        # the test_e2e.py file
        confirmPage = ConfirmPage(self.browser)
        return confirmPage