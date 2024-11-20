import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.implicitly_wait(5)
# driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()
driver.switch_to.window(driver.window_handles[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element(By.TAG_NAME, "h3").text)

