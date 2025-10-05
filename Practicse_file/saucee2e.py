import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    yield driver
    driver.quit()


def test_single_item_checkout_journey(driver):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    #user name and password
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
    elem.send_keys("standard_user")
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
    elem.send_keys("secret_sauce")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
    login_button.click()
    # Verify successful login by checking for the presence of the product page title
    products_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
    assert products_title.text == "Products"

    # Add an item to the cart
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_to_cart_button.click()

    # Navigate to the cart
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()

    # Verify item in cart and proceed to checkout
    cart_item = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']")))
    assert cart_item.is_displayed()

    checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_button.click()

    # Fill in checkout information
    first_name_field = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
    first_name_field.send_keys("John")

    last_name_field = wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
    last_name_field.send_keys("Doe")

    zip_code_field = wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
    zip_code_field.send_keys("12345")

    continue_button = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    continue_button.click()

    # Verify checkout overview and finish the order
    finish_button = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_button.click()

    # Verify order completion
    order_complete_header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    assert order_complete_header.text == "Thank you for your order!"
