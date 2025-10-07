import pytest
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver("chrome")
    yield driver
    driver.quit()
