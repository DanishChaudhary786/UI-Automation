import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))
assert results != 0

Expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]

Actual_Result = []
for result in results:
    Actual_Result.append(result.find_element(By.XPATH, "h4").text)

assert Actual_Result == Expected_list

for r in results:
    r.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum Validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
assert sum == int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discont_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
total_amount = float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert discont_amount < total_amount
time.sleep(2)
