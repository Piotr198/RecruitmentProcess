from selenium.webdriver.common.by import By
from Locators import Locator


class AddUser(object):

    def __init__(self, driver):
        self.driver = driver
        self.NewUserName=driver.find_element(By.XPATH, Locator.NewUserName)
        self.NewUserLastName=driver.find_element(By.XPATH, Locator.NewUserLastName)
        self.NewUserEmail=driver.find_element(By.XPATH, Locator.NewUserEmail)
        self.NewUserSubmitButton=driver.find_element(By.XPATH, Locator.NewUserSubmitButton)

    

    def setNewUserName(self, username):
        self.NewUserName.clear()
        self.NewUserName.send_keys(username)

    def setNewUserLastName(self, lastname):
        self.NewUserLastName.clear()
        self.NewUserLastName.send_keys(lastname)
    
    def setNewUserEmail(self, email):
        self.NewUserEmail.clear()
        self.NewUserEmail.send_keys(email)

    def clickNewUserSubmitButton(self):
        self.NewUserSubmitButton.click()

