from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.CART_ITEM = (By.CLASS_NAME, "cart_item")
        self.INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
        self.INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
        self.CART_REMOVE_BUTTON = (By.CLASS_NAME, "btn_secondary")
        self.CHECKOUT_BUTTON = (By.ID, "checkout")
        
    def remove_item(self, product_name):
        """Remove an item from the cart by its name."""
        cart_items = self.driver.find_elements(*self.CART_ITEM)
        for item in cart_items:
            item_name = item.find_element(*self.INVENTORY_ITEM_NAME).text
            if item_name == product_name:
                remove_button = item.find_element(*self.CART_REMOVE_BUTTON)
                remove_button.click()
                break
    
    def click_checkout(self):
        """Click the checkout button on the cart page."""
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()
