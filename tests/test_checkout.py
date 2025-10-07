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
def test_login(login_page):
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_at_home_page(), "Login failed"

@pytest.mark.order(2)
def test_add_products_and_verify_prices(checkout_page):
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    added_prices = checkout_page.add_products(products_to_add)
    assert checkout_page.get_cart_count() == len(products_to_add), "Not all products were added to the cart"
    cart_items = checkout_page.go_to_cart_and_get_items()
    for name in products_to_add:
        assert name in added_prices, f"Product {name} not found in inventory page."
        assert name in cart_items, f"Product {name} not found in cart."
        assert added_prices[name] == cart_items[name], f"Price mismatch for {name}: inventory={added_prices[name]}, cart={cart_items[name]}"

@pytest.mark.order(3)
def test_checkout_and_verify_message(checkout_page):
    checkout_page.proceed_to_checkout("John", "Doe", "12345")
    final_message = checkout_page.finish_and_get_message()
    assert "Thank you for your order!" in final_message, "Final checkout message not found!"

@pytest.mark.order(4)
def test_logout(login_page):
    login_page.logout()
