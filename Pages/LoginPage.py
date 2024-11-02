from selenium.webdriver.common.by import By


class loginpage:

    loc_username = (By.ID,"user-name")
    loc_password = (By.ID,"password")
    loc_login = (By.ID,"login-button")

    def __init__(self,driver):
        self.driver = driver

    def Username(self):
        return self.driver.find_element(*self.loc_username)

    def Password(self):
        return self.driver.find_element(*self.loc_password)

    def ClickLogin(self):
        return self.driver.find_element(*self.loc_login)

    def LoginPage(self):
        pass
