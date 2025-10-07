import pytest
from pages.logout_page import LogoutPage
from pages.login_page import LoginPage

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

def test_logout(login_page):
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    logout_page_instance = LogoutPage(login_page.driver)
    assert logout_page_instance.logout(), "Logout failed - Login button not displayed"
