import time

from selenium import webdriver


driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
title = driver.title
if "Rahul Shetty Academy" in title:
    print("Title Matched")
else:
    print("Title not matched")
time.sleep(3)
driver.quit()