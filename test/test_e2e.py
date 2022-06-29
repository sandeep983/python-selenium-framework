from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage

class TestOne(BaseClass):
    def test_e2e(self):
        '''We defined browser opening inside the 'setup method' in 'conftest.py'
            file we will use it with the help of fixture.'''

        #logger object
        log = self.getLogger()

        #passing browser/driver to homepage.py
        homePage = HomePage(self.browser)
        #click shop button and return and pass the browser/driver to CheckoutPage.py
        checkOutPage = homePage.getShopItems()
        

        #logging into log file
        log.info("getting all the card titles")
        #getting all the products/cards in page
        products = checkOutPage.getCardTitles()
        i = -1
        for product in products:
            i = i + 1
            productTitle = product.text
            #printing title of the product in log file
            log.info(productTitle)
            if (productTitle ==  'Blackberry'):
                checkOutPage.getAddToCart()[i].click()   

        #click checkout button
        checkOutPage.getCheckoutButton().click()
        #checkout button of next page
        #click checkout button on next page and return and pass the browser/driver to
        # ConfirmPage.py
        confirmPage = checkOutPage.getCheckoutButtonNext()

        #logging into log file
        log.info("Entering country name as ind")
        #input box - entering "ind"
        confirmPage.getInputBox().send_keys('ind')
        #verify the link presence
        self.verifyLinkPresence("India")
        #select/click india
        confirmPage.getSelectInd().click()

        #click on t&c checkbox
        confirmPage.getCheckBox().click()
        #click on purchase button
        confirmPage.getPurchaseButton().click()

        #get the success msg printed on webpage verify it if it's matching
        success_text = confirmPage.getSuccessMsg().text
        #logging the success msg into log file
        log.info("Text received from application is: " + success_text)
        assert "Success! Thank you!" in success_text


        #taking a screenshot of the page
        self.browser.get_screenshot_as_file('ss.png')