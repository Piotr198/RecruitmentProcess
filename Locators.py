class Locator(object):



# G_Email Page Locators
        G_Email="#identifierId"
        Next1="identifierNext"

# G_Password Page Locators
        G_Password="password"
        Next2="passwordNext"
        Unopened="//*[@class='zA zE']"

# MainGmail Page Locators
        Box="//*[@class='T-Jo-auh']"
        Delete="//*[@class='ar9 T-I-J3 J-J5-Ji']"
        


#Recover Password Page
        RecoverEmail="//*[@class='form-control valid required']"
        ButtonRecoverPassword="//*[@class='btn btn-primary']"
        #Textbox="//*[@class='alert alert-success']"


# Login Page locators
        Email="//*[@id='user-email']"
        Password="//*[@id='user-password']"
        LoginInButton="//*[@value='Zaloguj']"
        RecoverPassword="//*[contains(text(), 'Odzyskaj hasło')]"
    

# Users Page Locators
        CreateButton="//*[@href='http://qa-test.programa.pl/users/create']"

# AddUser Page Locators
        NewUserName="//*[contains(@id, 'firstname')]"
        NewUserLastName="//*[@name='model_User[lastname]']"
        NewUserEmail="//*[@name='model_User[email]']"
        NewUserSubmitButton="//*[@name='model_User[submit]']"








