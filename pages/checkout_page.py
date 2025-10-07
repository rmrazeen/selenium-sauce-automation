from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    # Class-level locators
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = (By.TAG_NAME, "button")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

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

    def go_to_cart_and_get_items(self):
        """Go to cart and return a dict of product name to price."""
        self.driver.find_element(*self.CART_ICON).click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        cart_items = {}
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            cart_items[name] = price
        return cart_items

    def proceed_to_checkout(self, first_name, last_name, postal_code):
        """Click checkout, fill info, and continue."""
        self.driver.find_element(By.ID, "checkout").click()
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def finish_and_get_message(self):
        """Click finish and return the final message text."""
        self.driver.find_element(By.ID, "finish").click()
        header = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
        return header.text
    
    # ...existing code...
