import pytest
from utilities.driver_factory import get_driver

@pytest.fixture(scope="function")
def setup():
    driver = get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield driver
    driver.quit()
