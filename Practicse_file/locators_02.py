from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Launch Chrome (Selenium will auto-manage ChromeDriver if v4.6+)
driver = webdriver.Chrome()

# Open python.org
driver.get("https://demoqa.com/radio-button")

# Find the search box
radio_button = driver.find_element(By.XPATH, "//label[normalize-space()='Yes']")
radio_button.click()
radio_v = driver.find_element(By.XPATH, "(//span[@class='text-success'])[1]")


# Verify results are found
assert "Yes"  == radio_v.text, f"Expected 'Yes' but got {radio_v.text}"
print("Test Passed")

# Close the browser window
driver.close()

#action chains for douuble click and right click
#webdriver wait

   