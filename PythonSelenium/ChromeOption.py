import time
from selenium import webdriver


chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")