from selenium.webdriver.common.by import By


class checkoutpage:

    loc_firstname = (By.XPATH,"//input[@data-test='firstName']")
    loc_lastname = (By.ID, "last-name")
    loc_zipcode = (By.CSS_SELECTOR, "input[data-test='postalCode']")
    loc_continue = (By.CSS_SELECTOR,"input[type='submit']")


    def __init__(self,driver):
        self.driver = driver

    def firstname(self):
        return self.driver.find_element(*self.loc_firstname)

    def lastname(self):
        return self.driver.find_element(*self.loc_lastname)

    def zipcode(self):
        return self.driver.find_element(*self.loc_zipcode)

    def Continue(self):
        return self.driver.find_element(*self.loc_continue)

