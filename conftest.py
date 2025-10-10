import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from asserts.login_assert import login_assertion

@pytest.fixture
def driver():
    driver = get_driver("chrome")
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def login_assert(driver):
    return login_assertion(driver)