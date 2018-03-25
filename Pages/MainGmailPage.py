from selenium.webdriver.common.by import By
from Locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainGmail(object):

    def __init__(self, driver):
        self.driver = driver

        self.Box=driver.find_element(By.XPATH, Locator.Box)
        self.Delete=driver.find_element(By.XPATH, Locator.Delete)
        self.Unopened=driver.find_elements(By.XPATH, Locator.Unopened)
      
        

    def clickBox(self):
        self.Box.click()
    
    def clickDelete(self,driver):
        self.Delete.click()
        assert "Twoja karta Główne jest pusta." in driver.page_source
        
