from selenium.webdriver import Keys

from .base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):
    def go_to_add_pet_page(self):
        self.browser.find_element(*ProfilePageLocators.ADD_PET_BTN).click()

    def go_to_edit_pet_page(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_PET_BTN).click()

    def show_popup_to_delete_pet_page(self):
        self.browser.find_element(*ProfilePageLocators.DELETE_PET_BTN).click()

    def delete_pet(self):
        self.browser.find_element(*ProfilePageLocators.CONFIRM_DELETE_POPUP_BTN).click()

    def edit_pet_age(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_PET_AGE).clear()
        self.browser.find_element(*ProfilePageLocators.EDIT_PET_AGE).send_keys("3", Keys.ENTER)

    def save_changes(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_PET_SAVE_BTN).submit()

