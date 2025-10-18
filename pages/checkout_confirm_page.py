from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class checkoutConfirmPage:
    # Class-level locators
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
 
    def finish_and_get_message(self):
        """Click finish and return the final message text."""
        self.driver.find_element(*self.FINISH_BUTTON).click()
        header = self.wait.until(EC.presence_of_element_located(self.COMPLETE_HEADER))
        return header.text

    def cancel_order(self):
        """Click the cancel button on the checkout confirmation page."""
        self.driver.find_element(*self.CANCEL_BUTTON).click()
