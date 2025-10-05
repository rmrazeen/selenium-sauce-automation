from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# Launch Chrome (Selenium will auto-manage ChromeDriver if v4.6+)
driver = webdriver.Chrome()

# Open python.org
print(driver.title)
driver.get("https://www.saucedemo.com/")
time.sleep(2)
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys("standard_user")
time.sleep(2)
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
time.sleep(2)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(2)

# Close the browser window

driver.quit()
#
