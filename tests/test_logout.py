import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.logout_page import logout_page
from pages.login_page import LoginPage

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument("--start-maximized")
    return options 

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

def test_logout(login_page):
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    logout_page_instance = logout_page(login_page.driver)
    assert logout_page_instance.logout(), "Logout failed - Login button not displayed"
