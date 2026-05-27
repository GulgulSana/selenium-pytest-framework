from operator import truediv
# number 11 created ddt
import pytest
from pageObjects.loginPage import LoginPage
from utilities.excelUtils import ExcelUtils

path = "testdata/loginData.xlsx"

@pytest.mark.regression
def test_loginn_ddt(setup):

    driver = setup
    login = LoginPage(driver)
    row = ExcelUtils.get_row_count(path,"Sheet1")

    for r in range(2,row+1):
        username = ExcelUtils.read_data(path,"Sheet1",r,1)
        password = ExcelUtils.read_data(path,"Sheet1",r,2)
        expected = ExcelUtils.read_data(path,"Sheet1",r,3)

        print(username, password, expected)

        if username is None:
            continue

        login.enter_username(username)
        login.enter_password(password)
        login.click_login()

        current_url = driver.current_url

        if "inventory" in current_url:

            if expected == "Pass":
                assert True
                driver.get("https://www.saucedemo.com/")

            else:
                assert False

        else:

            if expected == "Fail":
                assert True

            else:
                assert False
