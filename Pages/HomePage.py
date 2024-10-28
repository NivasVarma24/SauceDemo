from selenium.webdriver.common.by import By


class homepage:

    loc_homepage = (By.XPATH,"//div [@class='product_label']")
    loc_prodcutdetails = (By.XPATH,"//div [@class='inventory_item']")
    loc_cart = (By.CSS_SELECTOR,"span[class*='counter shopping_cart_badge']")


    def __init__(self,driver):
        self.driver = driver

    def productDetails(self):
        return self.driver.find_elements(*self.loc_prodcutdetails)

    def cart(self):
        return self.driver.find_element(*self.loc_cart)


