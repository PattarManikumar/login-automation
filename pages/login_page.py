from selenium.webdriver.common.by import By
from utilities.wait import Waits

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.waits = Waits(driver)

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")

    def login(self, user, pwd):
        self.waits.wait_for_visible(self.username).send_keys(user)
        self.waits.wait_for_visible(self.password).send_keys(pwd)
        self.waits.wait_for_clickable(self.login_btn).click()
