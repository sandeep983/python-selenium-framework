from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
import pytest


class TestHomepage(BaseClass):
    def test_homepageForm(self, getData):
        #logger object
        log = self.getLogger()

        #passing browser/driver to homepage.py
        homepage = HomePage(self.browser)
        #logging firstname into log file
        log.info("Firstname: " + getData["firstname"])
        #fill name in name field in the homepage form
        homepage.getName().send_keys(getData["firstname"])
        #fill email in email field in the homepage form
        homepage.getEmail().send_keys(getData["email"])
        #click on checkbox
        homepage.getCheck().click()

        #we are getting this from the Baseclass.py
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        #click on the submit button
        homepage.getSubmit().click()

        #checking if success text is present in homepage or not after we are done 
        # with the all the operations
        alertText = homepage.getSuccessMsg().text
        assert("Success" in alertText)

        self.browser.refresh()


    @pytest.fixture(params=HomePageData.test_homepageData)
    def getData(self, request):
        return request.param