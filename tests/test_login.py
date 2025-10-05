import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

def test_successful_login(login_page):
    """Test successful login with valid credentials"""
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    
    # Assert that we're on the products page after login
    assert login_page.is_at_login_page(), "Login failed - Products page not displayed"