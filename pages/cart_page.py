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
        self.CART_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
        self.CHECKOUT_BUTTON = (By.ID, "checkout")

    