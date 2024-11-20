import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
result = driver.find_elements(By.XPATH, "//tr/td[1]")
List = []
for r in result:
    List.append(r.text)

List1 = List.copy()
print(f"List1: {List1} and List: {List}")
List1.sort()
assert List1 == List
