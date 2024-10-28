from selenium.webdriver.common.by import By


class cartpage:

    loc_cartItem = (By.XPATH,"//div[@class='inventory_item_name']")
    loc_checkoutbtn = (By.XPATH,"//a[@class='btn_action checkout_button']")

    def __init__(self,driver):
        self.driver = driver

    def cartItemName(self):
        return self.driver.find_element(*self.loc_cartItem)

    def clickCheckout(self):
        return self.driver.find_element(*self.loc_checkoutbtn).click()