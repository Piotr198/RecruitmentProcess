from selenium.webdriver.common.by import By
from Locators import Locator


class Login(object):

    def __init__(self, driver):
        self.driver = driver

        self.Email = driver.find_element(By.XPATH, Locator.Email)
        self.Password = driver.find_element(By.XPATH, Locator.Password)
        self.RecoverPassword=driver.find_element(By.XPATH,Locator.RecoverPassword)
        self.LoginInButton=driver.find_element(By.XPATH,Locator.LoginInButton)


    def setEmail(self, username):
        self.Email.clear()
        self.Email.send_keys(username)

    def setPassword(self, password):
        self.Password.clear()
        self.Password.send_keys(password)
    
    def click_RecoverPassword(self):
        self.RecoverPassword.click()
    
    def click_LoginInButton(self):
        self.LoginInButton.click()

