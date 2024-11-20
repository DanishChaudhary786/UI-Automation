import time
from selenium import webdriver

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(options=chrome_option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0, 500);")
driver.get_screenshot_as_file("screen.png")
time.sleep(5)
