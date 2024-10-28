import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def browser(request):
    serobj = Service("C:\\Users\saini\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serobj)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/")
    request.cls.driver = driver
    yield
    driver.close()
