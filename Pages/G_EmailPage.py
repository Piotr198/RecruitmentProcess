from selenium.webdriver.common.by import By
from Locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class G_Email(object):

    def __init__(self, driver):
        self.driver = driver
        self.G_Email=driver.find_element(By.CSS_SELECTOR,Locator.G_Email)
        self.Next1=driver.find_element(By.ID, Locator.Next1)

    
    def setG_Email(self, username):
        self.G_Email.clear()
        self.G_Email.send_keys(username)

    def clickNext1(self,driver):
        self.Next1.click()
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, Locator.G_Password)))

