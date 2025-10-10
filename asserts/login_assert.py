from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class login_assertion:
    PRODUCTS_TITLE = (By.XPATH, "//span[@data-test='title']")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    
    def is_at_home_page(self):
        """Verify if we are on products page after login"""
        element = self.wait.until(
            EC.presence_of_element_located(self.PRODUCTS_TITLE)
        )
        return element.text == "Products"
    
    def validate_url(self, expected_url):
        """Verify if the current URL matches the expected URL"""
        return self.driver.current_url == expected_url
    
    def current_url(self):
        """Get the current URL of the page"""
        return self.driver.current_url
