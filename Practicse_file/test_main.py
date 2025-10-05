import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.mark.order(1)
def test_login(driver, wait):
    user_name = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    user_pass = driver.find_element(By.ID, "password")
    user_name.send_keys("standard_user")
    user_pass.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    inventory = wait.until(EC.presence_of_element_located((By.ID, "inventory_container")))
    assert inventory.is_displayed(), "Login failed or inventory page not loaded."
    print("Login successful, inventory page loaded.")

#helprer function
def add_products(driver, names):
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for product in products:
        pname = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        if pname in names:
            product.find_element(By.TAG_NAME, "button").click()



@pytest.mark.order(2)
def test_add_products(driver, products):
    products = ["Sauce Labs Backpack"]
    add_products(driver,products)
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_count = cart_icon.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    cart_count = int(cart_count) if cart_count else 0
    assert cart_count == len(products), f"Expected {len(products)} items in cart, but found {cart_count}."
    print(f"Added {cart_count} items to the cart successfully.")



@pytest.mark.order(3)
def test_check_out(driver, wait):
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()
    checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_button.click()
    first_name_field = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
    first_name_field.send_keys("John")
    last_name_field = wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
    last_name_field.send_keys("Doe")
    zip_code_field = wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
    zip_code_field.send_keys("12345")
    continue_button = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    continue_button.click()
    finish_button = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_button.click()
    order_complete_header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    assert order_complete_header.text == "Thank you for your order!"
    print("Order completed successfully.")

@pytest.mark.order(4)
def test_log_out(driver, wait):
    menu_button = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
    menu_button.click()
    logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
    logout_link.click()
    login_button = wait.until(EC.presence_of_element_located((By.ID, "login-button")))
    assert login_button.is_displayed(), "Logout failed or login page not loaded."
    print("Logout successful, login page loaded.")