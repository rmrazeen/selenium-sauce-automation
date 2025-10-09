import pytest
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def login_page(driver):
    """Provides a LoginPage instance using the shared driver fixture."""
    return LoginPage(driver)


@pytest.fixture
def checkout_page(driver):
    """Provides a CheckoutPage instance using the shared driver fixture."""
    return CheckoutPage(driver)


# ---------- TEST 1: LOGIN ----------
@pytest.mark.order(1)
def test_login(login_page):
    """Step 1: Verify user can log in successfully."""
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_at_home_page(), "Login failed - User not on home page"


# ---------- TEST 2: ADD PRODUCTS TO CART ----------
@pytest.mark.order(2)
def test_add_to_cart(login_page, checkout_page):
    """Step 2: Verify user can add products to the cart."""
    # Ensure we're on the products page
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_at_home_page(), "Not on products page"
    
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    checkout_page.add_products(products_to_add)
    cart_count = checkout_page.get_cart_count()
    assert cart_count == len(products_to_add), \
        f"Expected {len(products_to_add)} items in cart, got {cart_count}"


# ---------- TEST 3: VERIFY CART DETAILS ----------
@pytest.mark.order(3)
def test_cart_verification(login_page, checkout_page):
    """Step 3: Verify items and prices in the cart."""
    # Ensure we're on the products page first
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_at_home_page(), "Not on products page"
    
    # Add products to cart first
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    checkout_page.add_products(products_to_add)
    
    # Navigate to cart and get items
    cart_items = checkout_page.go_to_cart_and_get_items()
    expected_prices = {
        "Sauce Labs Backpack": "$29.99",
        "Sauce Labs Bike Light": "$9.99"
    }

    for product_name, actual_price in cart_items.items():
        assert product_name in expected_prices, f"Unexpected product '{product_name}' found"
        assert actual_price == expected_prices[product_name], \
            f"Price mismatch for {product_name}: expected {expected_prices[product_name]}, got {actual_price}"


# ---------- TEST 4: CHECKOUT PROCESS ----------
@pytest.mark.order(4)
def test_checkout(login_page, checkout_page):
    """Step 4: Verify user can complete checkout."""
    # Ensure we're on the products page first
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_at_home_page(), "Not on products page"
    
    # Add products to cart and navigate to cart
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    checkout_page.add_products(products_to_add)
    
    # Navigate to cart (this is needed before checkout)
    checkout_page.go_to_cart_and_get_items()
    
    # Now proceed with checkout
    checkout_page.proceed_to_checkout("John", "Doe", "12345")
    final_message = checkout_page.finish_and_get_message()
    assert "Thank you for your order!" in final_message, "Order success message not found"


# ---------- TEST 5: LOGOUT ----------
@pytest.mark.order(5)
def test_logout(login_page, checkout_page):
    """Step 5: Verify user can log out successfully."""
    # Ensure we're on the products page first (where logout is possible)
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_at_home_page(), "Not on products page"
    
    # Now we can logout
    login_page.logout()
    assert login_page.is_login_button_visible(), "Logout failed - Login button not displayed"
# ---------- COMBINED TEST: COMPLETE CHECKOUT FLOW ----------
