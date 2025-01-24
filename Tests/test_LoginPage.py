import time
from _ast import Assert

import pytest
import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.CartPage import cartpage
from Pages.HomePage import homepage
from Pages.LoginPage import loginpage
from Pages.OverViewPage import overview
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
        if loginpgobj.ClickLogin().is_enabled():
            loginpgobj.ClickLogin().click()
            print("Login Button is working")
        else:
            print("Login Button is not working")
        self.driver.refresh()

    def test_verifySuccesfullLogin(self):
        loginpgobj = loginpage(self.driver)
        loginpgobj.Username().send_keys("standard_user")
        loginpgobj.Password().send_keys("secret_sauce")
        loginpgobj.ClickLogin().click()

        homepgobj = homepage(self.driver)
        # wait = WebDriverWait(self.driver,10)
        # assert wait.until(expected_conditions.presence_of_element_located(homepgobj.loc_homepage))
        #Created common utilite for wait
        assert self.checkForElement(homepgobj.loc_homepage)
        products = homepgobj.productDetails()
        productName = "Sauce Labs Fleece Jacket"
        for product in products:
            if product.find_element(By.XPATH, "div[2]/a/div").text == productName:
                product.find_element(By.XPATH, "div[3]/button").click()
        time.sleep(3)
        # wait.until(expected_conditions.presence_of_element_located(homepgobj.loc_cart))
        #used common utility
        self.checkForElement(homepgobj.loc_cart)
        homepgobj.cart().click()

        cartpgobj = cartpage(self.driver)
        addedItem = cartpgobj.cartItemName().text

        if productName == addedItem:
            checkoutpgobj = cartpgobj.clickCheckout()
            print("Items Matched, Proceed to checkout")
            checkoutpgobj.firstname().send_keys("sai")
            checkoutpgobj.lastname().send_keys("nivas")
            checkoutpgobj.zipcode().send_keys("123456")
            checkoutpgobj.Continue().click()
        else:
            print("Items does not match")

        overviewpgobj = overview(self.driver)
        print('{}{}'.format("ItemCost: ",overviewpgobj.getSubtotal().text ))
        print('{}{}'.format("Tax: ", overviewpgobj.getTax().text ))
        print('{}{}'.format("Total: ", overviewpgobj.getTotal().text ))

        finsihobj = overviewpgobj.clickFinish()
        confirmMsg = finsihobj.succesmsg()
        print(confirmMsg)
        print(confirmMsg)
        print("hello")
        assert "THANK YOU" in confirmMsg























