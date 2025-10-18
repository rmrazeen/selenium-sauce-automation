from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = (By.TAG_NAME, "button")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_inventory(self):
        """Navigate to the Inventory page."""
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def add_products(self, product_names):
        """Add products to cart by their names. Accepts a list of product names."""
        products = self.driver.find_elements(*self.INVENTORY_ITEM)
        added_prices = {}
        for product in products:
            pname = product.find_element(*self.INVENTORY_ITEM_NAME).text
            if pname in product_names:
                product.find_element(*self.ADD_TO_CART_BUTTON).click()
                price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
                added_prices[pname] = price
        return added_prices
    
    def get_cart_count(self):
        """Return the number of items in the cart."""
        cart_icon = self.driver.find_element(*self.CART_ICON)
        try:
            cart_count = cart_icon.find_element(*self.CART_BADGE).text
            return int(cart_count)
        except Exception:
            return 0
            
    def click_cart_icon(self):
        """Click the cart icon to navigate to the cart page."""
        self.driver.find_element(*self.CART_ICON).click()
        
    def add_first_item_to_cart(self):
        """Add the first inventory item to cart."""
        first_item = self.driver.find_element(*self.INVENTORY_ITEM)
        first_item.find_element(*self.ADD_TO_CART_BUTTON).click()
        return self
        
    def click_checkout_button(self):
        """Click the checkout button on the cart page."""
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()
        return self
