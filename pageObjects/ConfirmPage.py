from ast import Pass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfirmPage:
    #to receive the driver/browser from the test_e2e.py, we need to define the constructor
    def __init__(self, browser):
        self.browser = browser


    #assigning the selector to shop variable for clicking the shop button
    inputBox = (By.CSS_SELECTOR, "#country")

    #type ind and search for it and then click on India option
    selectInd = (By.LINK_TEXT, "India")

    #t&c checkbox
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    #purchase button
    purchaseButton = (By.CSS_SELECTOR, "[type='submit']")

    #get success msg
    successMsg = (By.CLASS_NAME, "alert-success")


    def getInputBox(self):
        #that * tells it to take it as webelement, it deserializes it as tuple
        return self.browser.find_element(*ConfirmPage.inputBox)

    def getWaitForInd(self):
        return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((self.selectInd)))
    
    def getSelectInd(self):
        return self.browser.find_element(*ConfirmPage.selectInd)

    def getCheckBox(self):
        return self.browser.find_element(*ConfirmPage.checkBox)

    def getPurchaseButton(self):
        return self.browser.find_element(*ConfirmPage.purchaseButton)

    def getSuccessMsg(self):
        return self.browser.find_element(*ConfirmPage.successMsg)