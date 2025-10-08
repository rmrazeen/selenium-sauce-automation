import pytest
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)

@pytest.mark.order(1)
def test_checkout_journey(login_page, checkout_page):
    # Step 1: Login
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_at_home_page(), "Login failed"

    # Step 2: Add two products to cart
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    checkout_page.add_products(products_to_add)
    assert checkout_page.get_cart_count() == len(products_to_add), "Not all products were added to the cart"

    # Step 3: Go to cart and verify product prices
    cart_items = checkout_page.go_to_cart_and_get_items()
    expected_prices = {"Sauce Labs Backpack": "$29.99", "Sauce Labs Bike Light": "$9.99"}
    for name, price in cart_items.items():
        assert name in expected_prices, f"Unexpected product in cart: {name}"
        assert price == expected_prices[name], f"Price mismatch for {name}: expected {expected_prices[name]}, got {price}"

    # Step 4: Proceed to checkout and fill info
    checkout_page.proceed_to_checkout("John", "Doe", "12345")

    # Step 5: Verify final message after finishing checkout
    final_message = checkout_page.finish_and_get_message()
    assert "Thank you for your order!" in final_message, "Final checkout message not found!"

    # Step 6: Logout
    login_page.logout()
