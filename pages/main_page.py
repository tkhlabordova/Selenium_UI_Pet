from .base_page import BasePage
from .locators import MainPageLocators
from .variables import MainPageConstants
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_register_page(self):
        register_link = self.browser.find_element(*MainPageLocators.REGISTER_LINK)
        register_link.click()

    def dropdown_list_open(self):
        self.browser.find_element(*MainPageLocators.DROPDOWN_FILTER).click()

    def dropdown_filter_apply(self):
        self.browser.find_element(*MainPageLocators.DROPDOWN_FILTER_ITEM).click()

    def filter_by_name(self):
        self.browser.find_element(*MainPageLocators.FILTER_BY_NAME).send_keys(MainPageConstants.PET_NAME, Keys.ENTER)

    def go_to_detail_page(self):
        self.browser.find_element(*MainPageLocators.DETAILS_BTN).click()

