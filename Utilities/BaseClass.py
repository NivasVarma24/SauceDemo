import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser")
class Baseclass:


    def checkForElement(self,locator):
        wait = WebDriverWait(self.driver,10)
        return wait.until(EC.presence_of_element_located(locator))

