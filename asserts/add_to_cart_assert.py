def assert_cart_count(cart_count, expected_count):
    """Assert that cart count matches expected number of items.
    
    Args:
        cart_count (int): Actual number of items in cart
        expected_count (int): Expected number of items in cart
        
    Raises:
        AssertionError: If cart_count doesn't match expected_count
    """
    assert cart_count == expected_count, \
        f"Expected {expected_count} items in cart, got {cart_count}"
