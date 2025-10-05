from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time

# Launch Chrome (Selenium will auto-manage ChromeDriver if v4.6+)
def driver_setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def login_form(driver):
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()  # Maximize to avoid layout issues
    
    # Use WebDriverWait for better element handling
    wait = WebDriverWait(driver, 10)
    
    # Wait for page to fully load
    time.sleep(3)
    
    # Close any ads or overlays that might be present
    try:
        # Try to close any ad overlay
        close_ad = driver.find_element(By.CSS_SELECTOR, "[id*='close'], [class*='close'], [id*='dismiss']")
        close_ad.click()
        time.sleep(1)
    except:
        pass  # No ad found, continue
    
    # locators
    username_field = wait.until(EC.element_to_be_clickable((By.ID, "userName")))
    mail_field = wait.until(EC.element_to_be_clickable((By.ID, "userEmail")))
    address_field = wait.until(EC.element_to_be_clickable((By.ID, "currentAddress")))
    per_address_field = wait.until(EC.element_to_be_clickable((By.ID, "permanentAddress")))
    
    # Fill out the form
    username_field.clear()
    username_field.send_keys("testuser")
    time.sleep(1)
    
    mail_field.clear()
    mail_field.send_keys("d9Og9@example.com")
    time.sleep(1)
    
    address_field.clear()
    address_field.send_keys("123 Main St")
    time.sleep(1)
    
    per_address_field.clear()
    per_address_field.send_keys("456 Elm St")
    time.sleep(1)
    
    # Scroll to submit button to ensure it's visible
    submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit")))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(2)
    
    # Try multiple methods to click the submit button
    try:
        # Method 1: Regular click
        submit_button.click()
    except ElementClickInterceptedException:
        try:
            # Method 2: JavaScript click
            driver.execute_script("arguments[0].click();", submit_button)
        except:
            try:
                # Method 3: ActionChains click
                ActionChains(driver).move_to_element(submit_button).click().perform()
            except:
                # Method 4: Send Enter key to the form
                per_address_field.send_keys(Keys.TAB)
                time.sleep(1)
                driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ENTER)
    
    time.sleep(3)
    
    # Verify the form submission by checking if output appears
    try:
        output_section = wait.until(EC.presence_of_element_located((By.ID, "output")))
        if output_section.is_displayed():
            print("Form submitted successfully! Output section appeared.")
            
            # Check if the submitted data is displayed
            try:
                name_output = driver.find_element(By.ID, "name")
                if "testuser" in name_output.text:
                    print("Username verification successful!")
                else:
                    print("Username not found in output")
            except:
                print("Could not find name output element")
        else:
            print("Output section not visible")
    except:
        print("Form submission may have failed - output section not found")
    
    time.sleep(2)

def main():
    driver = driver_setup()
    try:
        login_form(driver)
        input("Press Enter to close the browser...")  # Keep browser open to see results
    finally:
        driver.quit()

# Execute the script
if __name__ == "__main__":
    main()