from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as webdriverwait
from selenium.webdriver.support import expected_conditions as EC

class logout_page:
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_button = (By.ID, "logout_sidebar_link")
    login_button = (By.ID, "login-button") 
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = webdriverwait(driver, 10)

    def logout(self):
        self.wait.until.EC.element_to_be_clicable(self.menu_button).click()
        self.wait.until.EC.element_to_be_clicable(self.logout_button).click()
        return self.wait.until(EC.presence_of_element_located(self.login_button)).is_displayed()