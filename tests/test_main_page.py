import pytest

from pages.main_page import MainPage
from pages.variables import MainPageConstants
import time


def test_go_to_login_page(browser):
    link = MainPageConstants.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('result_login_page.png')


def test_go_to_register_page(browser):
    link = MainPageConstants.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_register_page()
    browser.save_screenshot('result_register_page.png')


@pytest.mark.filters
def test_filter_dropdown(browser):
    link = MainPageConstants.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.dropdown_list_open()
    time.sleep(1)
    page.dropdown_filter_apply()
    time.sleep(1)
    browser.save_screenshot('filter_dropdown_result.png')


@pytest.mark.filters
def test_filter_by_name(browser):
    link = MainPageConstants.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.filter_by_name()
    time.sleep(2)
    browser.save_screenshot('filter_by_name_result.png')


def test_go_to_details_page(browser):
    link = MainPageConstants.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    time.sleep(1)
    page.go_to_detail_page()
    time.sleep(2)
    browser.save_screenshot('go_to_details_result.png')