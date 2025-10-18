from asserts.add_to_cart_assert import assert_cart_count


import pytest

# ---------- TEST ADD PRODUCTS TO CART ----------
@pytest.mark.smoke
def test_add_to_cart(login, inventory_page):
    """ Verify user can add products to the cart."""
    # items added in a variable 
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    
    # Add the specified products to the cart
    inventory_page.add_products(products_to_add)
    
    # Get the number of items in the cart
    cart_count = inventory_page.get_cart_count() # Retrieve cart count in a variable from the page get_cart_count() method
    
    # assertion function
    assert_cart_count(cart_count, len(products_to_add)) # compare actual count with expected count with len(products_to_add) for get the length of the list, which is 2 in this case and pass it to assert_cart_count from asserts/add_to_cart_assert.py and pass the cart_count variable and expected count as parameters
