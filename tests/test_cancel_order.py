import pytest
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_confirm_page import checkoutConfirmPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.regression
def test_cancel_order_from_checkout(login_page, inventory_page, cart_page, checkout_info_page, checkout_confirm_page):
    """Test that a user can cancel an order from the checkout confirmation page."""
    # Login
    login_page.login("standard_user", "secret_sauce")

    # Add products to cart
    inventory_page.add_products(["Sauce Labs Backpack"])

    # Go to cart
    inventory_page.click_cart_icon()

    # Proceed to checkout
    cart_page.click_checkout()

    # Fill checkout information
    checkout_info_page.fill_checkout_info("Jane", "Doe", "98765")

    # Cancel the order
    checkout_confirm_page.cancel_order()

    # Verify that the user is redirected to the inventory page
    assert "inventory.html" in inventory_page.driver.current_url, "User was not redirected to inventory page after canceling order"
    assert inventory_page.get_cart_count() == 0, "Cart was not empty after canceling order"
