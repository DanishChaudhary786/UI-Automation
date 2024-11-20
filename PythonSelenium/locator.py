import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("dc@wotnot.io")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("D@nish")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("DC")
# driver.find_element(By.CSS_SELECTOR, "inlineRadio1").click()

#Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("DC")
alert = driver.find_element(By.CLASS_NAME, 'alert-success').text
assert "Success" in alert
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(2)
