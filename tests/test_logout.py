import pytest

@pytest.mark.smoke
def test_logout(login, logout_page):
    """Test that user can logout successfully after login."""
    assert logout_page.logout(), "Logout failed - Login button not displayed"
