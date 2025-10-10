import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = get_driver("chrome")
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def login_assertion(driver):
    from asserts.login_assert import login_assertion
    return login_assertion(driver)