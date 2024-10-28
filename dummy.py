import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serobj = Service("C:\\Users\saini\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serobj)
driver.implicitly_wait(5)
driver.get("https://www.saucedemo.com/v1/inventory.html")
# username = driver.find_element(By.ID,"user-name")
# if username.is_enabled():
#     print("enabled")
# else:
#     ("disabled")
#
# login =  driver.find_element(By.ID,"login-button")
# if login.is_enabled():
#     login.click()
# else:
#     print("unable to clcik")
#
#
# name = driver.find_element(By.XPATH,"//div [@class='product_label']")
#
prod_name = driver.find_elements(By.XPATH,"//div [@class='inventory_item']/div[2]/a/div")

for i in prod_name:
    print(i.text)
# print(prod_name.text)

# print(name)

time.sleep(5)

