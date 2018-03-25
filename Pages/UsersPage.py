from selenium.webdriver.common.by import By
from Locators import Locator


class Users(object):

    def __init__(self, driver):
        self.driver = driver

        self.CreateButton = driver.find_element(By.XPATH, Locator.CreateButton)
        


    def click_CreateButton(self):
        self.CreateButton.click()

