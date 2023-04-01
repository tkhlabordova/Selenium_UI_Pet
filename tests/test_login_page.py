import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import ProfilePageLocators
from pages.login_page import LoginPage
from pages.variables import LoginPageConstants


@pytest.mark.login
def test_go_to_login(browser):
    link = LoginPageConstants.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.enter_email()
    page.enter_pass()
    page.submit_credentials()
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_PET_IMG))
    browser.save_screenshot('result_login.png')
