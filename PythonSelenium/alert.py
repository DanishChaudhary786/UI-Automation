import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys("Danish")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alert_text = alert.text
assert "Danish" in alert_text
alert.accept()

driver.find_element(By.ID, "name").send_keys("Danish")
driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
alert.dismiss()
driver.find_element(By.ID, "name").send_keys("DC")
driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
alert_text = alert.text
alert.accept()

