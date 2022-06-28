from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage

class TestHomepage(BaseClass):
    def test_homepageForm(self):
        #passing browser/driver to homepage.py
        homepage = HomePage(self.browser)
        #fill name in name field in the homepage form
        homepage.getName().send_keys("Sandeep")
        #fill email in email field in the homepage form
        homepage.getEmail().send_keys("sandeeppatel8878@gmail.com")
        #click on checkbox
        homepage.getCheck().click()

        #we are getting this from the Baseclass.py
        self.selectOptionByText(homepage.getGender(), "Male")
        #click on the submit button
        homepage.getSubmit().click()

        #checking if success text is present in homepage or not after we are done 
        # with the all the operations
        alertText = homepage.getSuccessMsg().text
        assert("Success" in alertText)


