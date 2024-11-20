import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 15)

# Open the webpage
driver.get("https://the-internet.herokuapp.com/iframe")

# Wait for the iframe to be available and switch to it
iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))

try:
    # Try to access an element inside the iframe to confirm the switch
    editor = driver.find_element(By.ID, "tinymce")
    print("Successfully switched to iframe. Editor found.")
    editor.clear()
except Exception as e:
    print

# Optionally wait to observe before closing
time.sleep(2)

# Close the driver
driver.quit()
