from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # Class-level locators
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCTS_TITLE = (By.XPATH, "//span[@data-test='title']")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def navigate_to(self, url):
        """Navigate to the login page"""
        self.driver.get(url)
        return self
        
    def enter_username(self, username):
        """Enter username in the username field"""
        username_element = self.wait.until(
            EC.presence_of_element_located(self.USERNAME_FIELD)
        )
        username_element.clear()
        username_element.send_keys(username)
        return self
        
    def enter_password(self, password):
        """Enter password in the password field"""
        password_element = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD_FIELD)
        )
        password_element.clear()
        password_element.send_keys(password)
        return self
        
    def click_login(self):
        """Click the login button"""
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()
        return self
        
    def login(self, username, password):
        """Perform complete login action"""
        return (self
                .enter_username(username)
                .enter_password(password)
                .click_login())
    

    def is_at_home_page(self):
        """Verify if we are on products page after login"""
        element = self.wait.until(
            EC.presence_of_element_located(self.PRODUCTS_TITLE)
        )
        return element.text == "Products"

    def logout(self):
        MENU_BUTTON = (By.ID, "react-burger-menu-btn")
        LOGOUT_LINK = (By.ID, "logout_sidebar_link")
        self.wait.until(EC.element_to_be_clickable(MENU_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(LOGOUT_LINK)).click()
        
    def is_login_button_visible(self):
        """Verify if the login button is visible (indicating we're on the login page)"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
            return True
        except:
            return False
