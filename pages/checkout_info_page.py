from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutInfoPage:
    # Class-level locators
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def fill_checkout_info(self, first_name, last_name, postal_code):
        """Fill checkout information and continue."""
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME_FIELD)).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_FIELD).send_keys(postal_code)
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()
        return self
