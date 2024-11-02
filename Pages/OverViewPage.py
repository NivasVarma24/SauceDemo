from selenium.webdriver.common.by import By

from Pages.finishPage import finishpage


class overview:

    loc_subtotal = (By.CSS_SELECTOR,"div[class='summary_subtotal_label']")
    loc_taxAmount = (By.CSS_SELECTOR,"div [class='summary_tax_label']")
    loc_total = (By.CSS_SELECTOR,"div [class='summary_total_label']")
    loc_finish = (By.CSS_SELECTOR,"a[class='btn_action cart_button']")

    def __init__(self,driver):
        self.driver = driver


    def getSubtotal(self):
        return self.driver.find_element(*self.loc_subtotal)

    def getTax(self):
        return self.driver.find_element(*self.loc_taxAmount)

    def getTotal(self):
        return self.driver.find_element(*self.loc_total)

    def clickFinish(self):
        self.driver.find_element(*self.loc_finish).click()
        finishpgObj = finishpage(self.driver)
        return  finishpgObj



