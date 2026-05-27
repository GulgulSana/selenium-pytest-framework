from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage
# number 9 using logger here
from utilities.logger import LogGen
# number 14 using config
from utilities.readProperties import ReadConfig
# number 15 pytest marker
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
# number 4 update testlogin with POM and conftest help
logger = LogGen.loggen()

@pytest.mark.sanity
def test_login(setup):
    print("Logger working")
    logger.info("test started")
    driver = setup  # driver called the output of setup fixture from conftest
    login = LoginPage(driver) # login is object of class LoginPage in POM

    logger.info("Entering username")
    login.enter_username(ReadConfig.get_username())

    logger.info("Entering password")
    login.enter_password(ReadConfig.get_password())

    logger.info("Clicking login button")
    login.click_login()

    assert "inventory" in driver.current_url

    logger.info("Test passed")

# number 1
# def test_login():
#     driver = webdriver.Chrome()
#
# # go to url
#     driver.get("https://www.saucedemo.com/")
#     driver.maximize_window()
# # enter username
#     driver.find_element(By.ID,"user-name").send_keys("standard_user")
# # enter password
#     driver.find_element(By.ID,"password").send_keys("secret_sauce")
#
# #click login
#     driver.find_element(By.ID,"login-button").click()
#     time.sleep(3)
#     assert "inventory" in driver.current_url
#
#     print("Login successful")
#
#     driver.quit()

