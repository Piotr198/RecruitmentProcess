from selenium.webdriver.common.by import By
from Locators import Locator


class RecoverPassword(object):

    def __init__(self, driver):
        self.driver = driver
   
        self.RecoverEmail=driver.find_element(By.XPATH, Locator.RecoverEmail)
        self.ButtonRecoverPassword=driver.find_element(By.XPATH, Locator.ButtonRecoverPassword)


    def setRecoverEmail(self, recoveremail):
        self.RecoverEmail.clear()
        self.RecoverEmail.send_keys(recoveremail)

    def click_ButtonRecoverPassword(self):
        self.ButtonRecoverPassword.click()








