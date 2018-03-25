import os, sys
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

import unittest
import time
from selenium import webdriver
from Locators import Locator
#from selenium.webdriver.common.by import By
from EnvironmentSetUp import EnvironmentSetup
from Pages.LoginPage import Login
from Pages.RecoverPasswordPage import RecoverPassword
from Pages.G_EmailPage import G_Email
from Pages.G_PasswordPage import G_Password
from Pages.MainGmailPage import MainGmail
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ResetPassword(EnvironmentSetup):
 
    def test_Programa(self):
        wwwGmail="https://accounts.google.com/signin/v2/sl/pwd?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"       
# Using the driver instances created in EnvironmentSetup 
        driver = self.driver
        self.driver.get(wwwGmail)
        self.driver.set_page_load_timeout(20)
# Entering Gmail for deleting all emails
# Creating object class G_EMAIL
        g_email=G_Email(driver)
        g_email.setG_Email("test1500101pro@gmail.com")
        g_email.clickNext1(driver)  
        print("2")
# Creating object class G_Password      
        g_password=G_Password(driver)
        g_password.setG_Password(driver,"TUTAJ WPISZ HASLO")
        g_password.clickNext2(driver)
        print("3")
# Creating object class MainGmail
#Deleting all emails
        maingmail=MainGmail(driver)
        maingmail.clickBox()
        if(len(maingmail.Unopened)!=0):
                maingmail.clickDelete(driver)
        print("4")


# Reset password on the RecoverPasswordPage
# Creating object recoverpassword
        wwwTestPrograma="http://qa-test.programa.pl/user/password/recover"
        self.driver.get(wwwTestPrograma)
        recoverpassword=RecoverPassword(driver)
        recoverpassword.setRecoverEmail("test1500101pro@gmail.com")
        recoverpassword.click_ButtonRecoverPassword()
# Assertion to be sure that everything is good
        assert "Email z linkiem do resetowania hasła został wysłany" in driver.page_source
        print("5")
        self.driver.get(wwwGmail)
        assert "Otrzymaliśmy wniosek o ustalenie nowego hasła." in driver.page_source  
        print("6")
      

if __name__ == '__main__':
    unittest.main()
