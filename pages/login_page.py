from .base_page import BasePage
from .locators import LoginPageLocators
from .variables import LoginPageConstants


class LoginPage(BasePage):
    def enter_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(LoginPageConstants.LOGIN_EMAIL)

    def enter_pass(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys(LoginPageConstants.LOGIN_PASS)

    def submit_credentials(self):
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.submit()

