import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxs = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxs:
    if checkbox.get_attribute("value") == "option1":
        checkbox.click()
        assert checkbox.is_selected()
        break


Radios = driver.find_elements(By.XPATH, "//input[@type='radio']")

for radio in Radios:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        assert radio.is_selected()
        break

driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert driver.find_element(By.ID, "displayed-text").is_displayed() == False