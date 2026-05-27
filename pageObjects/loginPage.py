# number 3

from selenium.webdriver.common.by import By


class LoginPage:

    textbox_username_id = 'user-name'
    textbox_password = 'password'
    button_login_id = 'login-button'

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self,username):
        username_box = self.driver.find_element(By.ID, self.textbox_username_id)
        username_box.clear()
        username_box.send_keys(username)
        # self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self,password):
        password_box = self.driver.find_element(By.ID, self.textbox_password)
        password_box.clear()
        password_box.send_keys(password)
        # self.driver.find_element(By.ID, self.textbox_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.button_login_id).click()