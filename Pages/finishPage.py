from selenium.webdriver.common.by import By


class finishpage:

    loc_successMsg = (By.CSS_SELECTOR,"h2[class='complete-header']")

    def __init__(self,driver):
        self.driver = driver

    def succesmsg(self):
        return self.driver.find_element(*self.loc_successMsg).text

