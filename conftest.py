import pytest
import os
from datetime import datetime
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from asserts.login_assert import login_assertion
from pages.logout_page import LogoutPage
from pages.inventory_page import InventoryPage
from pages.inventory_page import InventoryPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.cart_page import CartPage
from pages.checkout_confirm_page import checkoutConfirmPage

# Pytest hook for taking screenshots on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            screenshot_dir = "report/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            test_name = item.name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{test_name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved: {screenshot_path}")
            report.extra = [
                {"_html": f'<div><img src="screenshots/{screenshot_name}" alt="screenshot" style="width:300px;height:200px;" onclick="window.open(this.src)" align="right"/></div>'}
            ]

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

# inventory page fixture
@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)


@pytest.fixture
def checkout_info_page(driver):
    """Provides a CheckoutInfoPage instance using the shared driver fixture."""
    return CheckoutInfoPage(driver)

@pytest.fixture
def cart_page(driver):
    """Provides a CartPage instance using the shared driver fixture."""
    return CartPage(driver)

@pytest.fixture
def checkout_confirm_page(driver):
    """Provides a checkoutConfirmPage instance using the shared driver fixture."""
    return checkoutConfirmPage(driver)

@pytest.fixture
def login(login_page,login_assert):
    """Fixture that logs in a user before each test."""
    login_page.login("standard_user", "secret_sauce")
    assert login_assert.is_at_home_page(), "Login failed - User not on home page"
    assert login_assert.validate_url("https://www.saucedemo.com/inventory.html"), "URL mismatch after login"
    yield
