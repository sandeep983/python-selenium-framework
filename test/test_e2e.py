from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage

class TestOne(BaseClass):
    def test_e2e(self):
        '''We defined browser opening inside the 'setup method' in 'conftest.py'
            file we will use it with the help of fixture.'''
        

        #passing browser/driver to homepage.py
        homePage = HomePage(self.browser)
        #click shop button
        homePage.getShopItems().click()
        


        #passing the browser/driver to checkoutpage.py
        checkOutPage = CheckOutPage(self.browser)

        #getting all the products/cards in page
        products = checkOutPage.getCardTitles()
        i = -1
        for product in products:
            i = i + 1
            productTitle = product.text
            if (productTitle ==  'Blackberry'):
                checkOutPage.getAddToCart()[i].click()   

        #click checkout button
        checkOutPage.getCheckoutButton().click()
        #checkout button of next page
        checkOutPage.getCheckoutButtonNext().click()

        

        #passing the browser/driver to confirmpage.py
        confirmPage = ConfirmPage(self.browser)

        #input box - entering "ind"
        confirmPage.getInputBox().send_keys('ind')
        #wait till the link text India is present and then click on it
        confirmPage.getWaitForInd()

        #select india
        confirmPage.getSelectInd().click()

        #click on t&c checkbox
        confirmPage.getCheckBox().click()
        #click on purchase button
        confirmPage.getPurchaseButton().click()

        #get the success msg printed on webpage verify it if it's matching
        success_text = confirmPage.getSuccessMsg().text
        assert "Success! Thank you!" in success_text



        #taking a screenshot of the page
        self.browser.get_screenshot_as_file('ss.png')