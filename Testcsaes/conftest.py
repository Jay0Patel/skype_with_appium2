import pytest
from appium import webdriver


# emulator
@pytest.fixture(scope="class")
def setup(request):
    capabilities = {
        "platformName": 'Android',
        "automationName": 'uiautomator2',
        "deviceName": 'emulator-5554',
        "appPackage": 'com.skype.raider',
        "appActivity": 'com.skype4life.MainActivity',
        # "noReset": True,
        # "fullReset": False
    }

    driver = webdriver.Remote("http://localhost:4723", capabilities)
    request.cls.driver = driver
    yield
    driver.quit()
