import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from asserts.add_to_cart_assert import assert_cart_count

# ---------- TEST REMOVE ITEM FROM CART ----------
@pytest.mark.sanaity
def test_remove_item(login, inventory_page):
    """ Verify user can remove a product from the cart."""
    # Add products to cart
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    inventory_page.add_products(products_to_add)
    
    # Navigate to cart
    inventory_page.click_cart_icon()
    
    # Initialize cart page
    cart_page = CartPage(inventory_page.driver)
    
    # Get initial cart count
    initial_cart_count = inventory_page.get_cart_count()
    
    # Remove the item from cart
    cart_page.remove_item("Sauce Labs Backpack")
    
    # Get updated cart count
    updated_cart_count = inventory_page.get_cart_count()
    
    # Verify cart count decreased
    assert updated_cart_count == initial_cart_count - 1, "Cart count did not decrease after removing item"
