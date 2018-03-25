from selenium.webdriver.common.by import By
from Locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class G_Password(object):

    def __init__(self, driver):
        self.driver = driver
        self.G_Password=driver.find_element(By.NAME,Locator.G_Password)
        self.Next2=driver.find_element(By.ID, Locator.Next2)

    
    def setG_Password(self,driver,password):
        self.G_Password.clear()
        self.G_Password.send_keys(password)
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, Locator.Next2)))

    def clickNext2(self,driver):
        self.Next2.click()
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, Locator.Box)))

 

        
