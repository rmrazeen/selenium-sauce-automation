from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_confirm_page import checkoutConfirmPage

import pytest

@pytest.mark.regression
def test_confirm_order(login_page, inventory_page, cart_page, checkout_info_page, checkout_confirm_page):
    # Login
    login_page.login("standard_user", "secret_sauce")

    # Add products to cart
    inventory_page.add_products(["Sauce Labs Backpack", "Sauce Labs Bike Light"])

    # Go to cart
    inventory_page.click_cart_icon()

    # Proceed to checkout
    cart_page.click_checkout()

    # Fill checkout information
    checkout_info_page.fill_checkout_info("John", "Doe", "12345")

    # Confirm order and get message
    final_message = checkout_confirm_page.finish_and_get_message()
    assert "Thank you for your order!" in final_message, "Order success message not found"

    # Logout
    login_page.logout()
    assert login_page.is_login_button_visible(), "Logout failed - Login button not displayed"
