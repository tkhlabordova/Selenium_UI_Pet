import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.variables import LoginPageConstants


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    go_to_login(browser)
    yield browser
    browser.quit()


def go_to_login(browser):
    link = LoginPageConstants.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.enter_email()
    page.enter_pass()
    page.submit_credentials()


