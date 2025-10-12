def test_login(logged_in_user, login_assert):
    """Step 1: Verify user can log in successfully."""
    assert logged_in_user.is_at_home_page(), "Login failed - User not on home page"
    assert login_assert.validate_url("https://www.saucedemo.com/inventory.html"), "URL mismatch after login"
