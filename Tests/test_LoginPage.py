import time

import pytest
import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.CartPage import cartpage
from Pages.HomePage import homepage
from Pages.LoginPage import loginpage
from Utilities.BaseClass import Baseclass


# @pytest.mark.usefixtures("browser")
#Baseclass gets the browser from BaseClass(File) which is using fixture
class TestLoginPage(Baseclass):

    def test_verifyUserName(self):
        loginpgobj = loginpage(self.driver)
        if loginpgobj.Username().is_enabled():
            loginpgobj.Username().send_keys("TEST TEXT")
            time.sleep(3)
            print("username is enabled")
        else:
            print("username is disabled")
        self.driver.refresh()


    def test_verifyPassword(self):
        loginpgobj = loginpage(self.driver)
        if loginpgobj.Password().is_enabled():
            loginpgobj.Password().send_keys("Password")
            time.sleep(3)
            print("Password is enabled")

        else:
            print("Password is Disabled")
        self.driver.refresh()


    def test_verifyLoginButton(self):
        loginpgobj = loginpage(self.driver)
        if loginpgobj.Login().is_enabled():
            loginpgobj.Login().click()
            print("Login Button is working")
        else:
            print("Login Button is not working")
        self.driver.refresh()

    def test_verifySuccesfullLogin(self):
        loginpgobj = loginpage(self.driver)
        loginpgobj.Username().send_keys("standard_user")
        loginpgobj.Password().send_keys("secret_sauce")
        loginpgobj.Login().click()

        homepgobj = homepage(self.driver)
        wait = WebDriverWait(self.driver,10)
        assert wait.until(expected_conditions.presence_of_element_located(homepgobj.loc_homepage))
        products = homepgobj.productDetails()
        productName = "Sauce Labs Fleece Jacket"
        for product in products:
            if product.find_element(By.XPATH, "div[2]/a/div").text == productName:
                product.find_element(By.XPATH, "div[3]/button").click()
        time.sleep(3)
        wait.until(expected_conditions.presence_of_element_located(homepgobj.loc_cart))
        homepgobj.cart().click()

        cartpgobj = cartpage(self.driver)
        addedItem = cartpgobj.cartItemName().text

        if productName == addedItem:
            cartpgobj.clickCheckout()
        else:
            print("Items does not match")

















