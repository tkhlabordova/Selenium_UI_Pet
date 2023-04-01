import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from conftest import go_to_login
from pages.locators import ProfilePageLocators
from pages.profile_page import ProfilePage
from pages.variables import ProfilePageConstants


def test_go_to_add_pet(browser):
    # go_to_login(browser)
    link = ProfilePageConstants.PROFILE_PAGE_URL
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_add_pet_page()
    time.sleep(2)
    browser.save_screenshot('result_go_to_AddPet_page.png')


@pytest.mark.edit_pet
def test_go_to_edit_pet(browser):
    # go_to_login(browser)
    link = ProfilePageConstants.PROFILE_PAGE_URL
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_edit_pet_page()
    time.sleep(2)
    browser.save_screenshot('result_go_to_EditPet_page.png')


@pytest.mark.edit_pet
def test_edit_pet(browser):
    # go_to_login(browser)
    link = ProfilePageConstants.PROFILE_PAGE_URL
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_edit_pet_page()
    time.sleep(2)
    page.edit_pet_age()
    time.sleep(2)
    page.save_changes()
    time.sleep(2)


def test_delete_pet(browser):
    # go_to_login(browser)
    link = ProfilePageConstants.PROFILE_PAGE_URL
    page = ProfilePage(browser, link)
    page.open()
    page.show_popup_to_delete_pet_page()
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located(ProfilePageLocators.CONFIRM_DELETE_POPUP))
    browser.save_screenshot('result_show_popup_to_delete_pet.png')
    page.delete_pet()
    time.sleep(2)
    browser.save_screenshot('result_deleted_pet.png')
