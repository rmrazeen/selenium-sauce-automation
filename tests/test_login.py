import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

def test_successful_login(login_page):
    """Test successful login with valid credentials"""
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_at_home_page(), "Login failed - Products page not displayed"