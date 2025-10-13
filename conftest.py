import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from asserts.login_assert import login_assertion
from pages.logout_page import LogoutPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
# ---------- FIXTURES ----------
# Shared driver fixture for all tests
@pytest.fixture
def driver():
    driver = get_driver("chrome")
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

# login fixtures
@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

# assert fixtures
@pytest.fixture
def login_assert(driver):
    return login_assertion(driver)

#logout fixture
@pytest.fixture
def logout_page(driver):
    return LogoutPage(driver)

@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)


@pytest.fixture
def checkout_page(driver):
    """Provides a CheckoutPage instance using the shared driver fixture."""
    return CheckoutPage(driver)

@pytest.fixture
def login(login_page,login_assert):
    """Fixture that logs in a user before each test."""
    login_page.login("standard_user", "secret_sauce")
    assert login_assert.is_at_home_page(), "Login failed - User not on home page"
    assert login_assert.validate_url("https://www.saucedemo.com/inventory.html"), "URL mismatch after login"
    yield
