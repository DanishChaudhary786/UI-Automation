import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
print(len(products))

for product in products:
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
driver.find_element(By.ID, "country").send_keys("Ind")
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
success = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in success
time.sleep(4)
driver.close()
