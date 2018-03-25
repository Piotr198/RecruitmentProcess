import os, sys
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

import unittest
import time
import random
import string
from selenium import webdriver
from Locators import Locator
from EnvironmentSetUp import EnvironmentSetup
from Pages.LoginPage import Login
from Pages.RecoverPasswordPage import RecoverPassword
from Pages.G_EmailPage import G_Email
from Pages.G_PasswordPage import G_Password
from Pages.MainGmailPage import MainGmail
from Pages.UsersPage import Users
from Pages.AddUserPage import AddUser

class AddNewUser(EnvironmentSetup):

    def test_Programa(self):
        wwwPrograma="http://qa-test.programa.pl/users"
# Using the driver instances created in EnvironmentSetup 
        driver = self.driver
        self.driver.get(wwwPrograma)
        self.driver.set_page_load_timeout(20)

# Creating object class Login
# Log into 
        email="test1500101pro@gmail.com"
        password="TUTAJ WPISZ HASLO"       
        login=Login(driver)
        login.setEmail(email)
        login.setPassword(password)
        login.click_LoginInButton()
        time.sleep(2)
# Creating object class Users
        users=Users(driver)
        users.click_CreateButton()
# Creating object class AddUser
        
        adduser=AddUser(driver)
        adduser.setNewUserName("User created automatically")
        adduser.setNewUserLastName("test")
        string.letters="abcdefghijklmnopqrstuvwxyz"
        email=""
        for x in range(15):
            letter=random.choice(string.letters)
            email=email+letter
        adduser.setNewUserEmail(email+"@gmail.com")
        adduser.clickNewUserSubmitButton()
        print("User was created")
        assert "Utworzono" in driver.page_source



if __name__ == '__main__':
    unittest.main()
