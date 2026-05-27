# number 2
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import ReadConfig

@pytest.fixture
def setup():
    driver = webdriver.Chrome(
        service = Service(ChromeDriverManager().install())
    )

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver.maximize_window()
    driver.get(ReadConfig.get_application_url())

    yield driver

    driver.quit()
# number 6 update the conftest with new fixture for screenshot
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call'and rep.failed:
        driver = item.funcargs['setup']
        driver.save_screenshot("sscreenshots/" + item.name + ".png")

