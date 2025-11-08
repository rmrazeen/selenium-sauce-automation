import pytest
import sys
import random
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

# ---------- PYTEST MARKERS DEMONSTRATION ----------

# 1. pytest.mark.skip - Unconditional skipping
@pytest.mark.skip(reason="This test is skipped for demonstration purposes")
def test_unconditional_skip(login, inventory_page):
    """Test that demonstrates unconditional skipping using pytest.mark.skip"""
    inventory_page.add_first_item_to_cart()
    assert inventory_page.get_cart_count() == 1

# 2. pytest.mark.skipif - Conditional skipping
@pytest.mark.skipif(sys.version_info < (3, 8), reason="Test requires Python 3.8 or higher")
def test_conditional_skip_python_version(login, inventory_page):
    """Test that demonstrates conditional skipping based on Python version"""
    inventory_page.add_first_item_to_cart()
    assert inventory_page.get_cart_count() == 1

# 3. pytest.mark.xfail - Expected failure handling
@pytest.mark.xfail(reason="This test is expected to fail due to invalid credentials")
def test_expected_failure(login_page):
    """Test that demonstrates expected failure handling using pytest.mark.xfail"""
    login_page.login("invalid_user", "invalid_password")
    assert login_page.is_at_home_page(), "Login should have failed"

# 4. pytest.mark.flaky - Retry logic for unstable tests
@pytest.mark.flaky(max_runs=3, min_passes=1, delay=2)
def test_unstable_test():
    """Test that demonstrates retry logic for unstable tests using pytest.mark.flaky"""
    # Simulate an unstable operation that might fail randomly
    if random.random() < 0.5:  # 50% chance of failure
        raise Exception("Random failure for demonstration")
    
    # This would be a real test in practice
    assert True, "Test passed after potential retry"

# 5. pytest.mark.dependency - Dependent test execution
@pytest.mark.dependency(name="login_test")
def test_dependency_login(login, inventory_page):
    """Test that demonstrates dependency marker - this test should pass"""
    inventory_page.add_first_item_to_cart()
    assert inventory_page.get_cart_count() == 1

@pytest.mark.dependency(depends=["login_test"])
def test_dependency_dependent_test(login, inventory_page):
    """Test that depends on login_test - will only run if login_test passes"""
    inventory_page.add_products(["Sauce Labs Bike Light"])
    assert inventory_page.get_cart_count() == 2

@pytest.mark.dependency(depends=["login_test"])
def test_dependency_another_dependent_test(login, inventory_page):
    """Another test that depends on login_test"""
    # Remove an item from cart
    inventory_page.click_cart_icon()
    cart_page = CartPage(inventory_page.driver)
    cart_page.remove_first_item()
    assert inventory_page.get_cart_count() == 0

# 6. pytest.mark.parametrize - Parameterized test data
@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("problem_user", "secret_sauce", True),
    ("performance_glitch_user", "secret_sauce", True)
])
def test_parameterized_login(login_page, login_assert, username, password, expected):
    """Test that demonstrates parameterized test data using pytest.mark.parametrize"""
    login_page.login(username, password)
    
    if expected:
        assert login_page.is_at_home_page(), f"Login failed for user: {username}"
        assert login_assert.validate_url("https://www.saucedemo.com/inventory.html"), f"URL mismatch for user: {username}"
    else:
        assert not login_page.is_at_home_page(), f"Login should have failed for user: {username}"

# 7. Combined markers example
@pytest.mark.smoke
@pytest.mark.skipif(sys.version_info < (3, 7), reason="Test requires Python 3.7 or higher")
@pytest.mark.parametrize("product_name", [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt"
])
def test_combined_markers(login, inventory_page, product_name):
    """Test that demonstrates combined markers with parametrize"""
    inventory_page.add_products([product_name])
    assert inventory_page.get_cart_count() == 1, f"Failed to add {product_name} to cart"

# 8. Skip with condition based on test data
@pytest.mark.parametrize("test_input,expected", [
    (2, 4),
    (3, 6),
    (4, 8),
    (5, 10)
])
@pytest.mark.skipif(condition=lambda: test_input > 3, reason="Skipping values greater than 3")
def test_skip_with_condition(test_input, expected):
    """Test that demonstrates conditional skipping based on test data"""
    assert test_input * 2 == expected, f"Expected {expected} but got {test_input * 2}"

# 9. Xfail with parametrize
@pytest.mark.parametrize("username,password", [
    ("locked_out_user", "secret_sauce"),
    ("invalid_user", "invalid_password")
])
@pytest.mark.xfail(reason="These users are expected to fail login")
def test_xfail_with_parametrize(login_page, username, password):
    """Test that demonstrates xfail with parametrize"""
    login_page.login(username, password)
    assert login_page.is_at_home_page(), f"Login should have failed for {username}"

# 10. Complex dependency example
@pytest.mark.dependency(name="setup_test")
def test_setup_dependency(login, inventory_page):
    """Setup test that adds items to cart"""
    products = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    inventory_page.add_products(products)
    assert inventory_page.get_cart_count() == len(products)

@pytest.mark.dependency(depends=["setup_test"])
def test_dependency_1(login, inventory_page):
    """Test that depends on setup_test"""
    inventory_page.click_cart_icon()
    cart_page = CartPage(inventory_page.driver)
    assert cart_page.get_item_count() == 2

@pytest.mark.dependency(depends=["setup_test"])
def test_dependency_2(login, inventory_page):
    """Another test that depends on setup_test"""
    inventory_page.remove_first_item_from_cart()
    assert inventory_page.get_cart_count() == 1

# 11. Flaky with parametrize
@pytest.mark.parametrize("attempts", [1, 2, 3])
@pytest.mark.flaky(max_runs=3, min_passes=1, delay=1)
def test_flaky_with_parametrize(attempts):
    """Test that demonstrates flaky with parametrize"""
    # Simulate a test that might fail on first attempts
    if attempts < 3:
        raise Exception(f"Failed on attempt {attempts}")
    assert attempts == 3, f"Test should have passed on attempt 3, but failed on {attempts}"

# 12. Skip based on environment variable
import os
@pytest.mark.skipif(os.environ.get("SKIP_LONG_TESTS") == "1", reason="Long tests skipped via environment variable")
def test_skip_based_on_environment(login, inventory_page):
    """Test that demonstrates skipping based on environment variable"""
    # This would be a longer running test in a real scenario
    inventory_page.add_first_item_to_cart()
    assert inventory_page.get_cart_count() == 1
