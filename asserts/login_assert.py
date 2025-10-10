from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class login_assert:
    def __init__(self, driver):
        self.driver = self.driver
        self.wait = self.WebDriverWait(driver, 10)

    
    def is_at_home_page(self):
        """Check if the user is on the home/products page after login."""
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "inventory_container")))
            return True
        except Exception:
            return False