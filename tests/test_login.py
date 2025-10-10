def test_login(login_page):
    """Step 1: Verify user can log in successfully."""
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_at_home_page(), "Login failed - User not on home page"
