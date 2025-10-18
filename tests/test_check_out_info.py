import pytest
import random
import string
from selenium.webdriver.common.by import By
from pages.checkout_info_page import CheckoutInfoPage


def generate_random_name(length=8):
    """Generate a random name with specified length."""
    return ''.join(random.choices(string.ascii_letters, k=length)).capitalize()


def generate_random_postal_code():
    """Generate a random postal code (numeric)."""
    return ''.join(random.choices(string.digits, k=5))


@pytest.mark.regression
def test_checkout_info_with_random_data(login, inventory_page, checkout_info_page):
    """Test filling checkout information with random data."""
    # Add an item to cart first
    inventory_page.add_first_item_to_cart()
    
    # Go to cart
    inventory_page.click_cart_icon()
    
    # Click checkout button
    inventory_page.click_checkout_button()
    
    # Generate random data
    first_name = generate_random_name()
    last_name = generate_random_name()
    postal_code = generate_random_postal_code()
    
    # Fill checkout information
    checkout_info_page.fill_checkout_info(first_name, last_name, postal_code)
    
    # Verify URL has changed to checkout overview page
    assert "/checkout-step-two.html" in checkout_info_page.driver.current_url, \
        f"Expected to be on checkout overview page, but current URL is: {checkout_info_page.driver.current_url}"
    
    # Verify that we can see the item in the cart overview
    item_name_element = checkout_info_page.driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert item_name_element.is_displayed(), "Item name should be visible in checkout overview"


@pytest.mark.sanaity
def test_checkout_info_with_empty_fields(login, inventory_page, checkout_info_page):
    """Test checkout with empty fields to verify error handling."""
    # Add an item to cart first
    inventory_page.add_first_item_to_cart()
    
    # Go to cart
    inventory_page.click_cart_icon()
    
    # Click checkout button
    inventory_page.click_checkout_button()
    
    # Try to proceed with empty fields
    checkout_info_page.driver.find_element(CheckoutInfoPage.CONTINUE_BUTTON[0], CheckoutInfoPage.CONTINUE_BUTTON[1]).click()
    
    # Verify error message is displayed
    error_message = checkout_info_page.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Error: First Name is required" in error_message, \
        f"Expected error message about first name being required, but got: {error_message}"


@pytest.mark.regression
def test_checkout_info_with_special_characters(login, inventory_page, checkout_info_page):
    """Test checkout with special characters in fields."""
    # Add an item to cart first
    inventory_page.add_first_item_to_cart()
    
    # Go to cart
    inventory_page.click_cart_icon()
    
    # Click checkout button
    inventory_page.click_checkout_button()
    
    # Test data with special characters
    first_name = "José-Maria"
    last_name = "O'Connor"
    postal_code = "12345"
    
    # Fill checkout information
    checkout_info_page.fill_checkout_info(first_name, last_name, postal_code)
    
    # Verify URL has changed to checkout overview page
    assert "/checkout-step-two.html" in checkout_info_page.driver.current_url, \
        f"Expected to be on checkout overview page, but current URL is: {checkout_info_page.driver.current_url}"
