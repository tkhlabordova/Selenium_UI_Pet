from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    REGISTER_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a > span')
    DROPDOWN_FILTER = (By.ID, 'typesSelector')
    DROPDOWN_FILTER_ITEM = (By.CSS_SELECTOR, 'li#pv_id_2_3.p-dropdown-item')
    FILTER_BY_NAME = (By.ID, 'petName')
    DETAILS_BTN = (By.XPATH, "//div[@id='app']/main/div/div[2]/div[2]/div/div/div/div[3]/div/button/span")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    PROFILE_PET_IMG = By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(1)' \
                                       ' > div > img'
    ADD_PET_BTN = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) > button')
    EDIT_PET_BTN = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(1) > '
                                     'div > div.product-list-action > button:nth-child(1)')
    DELETE_PET_BTN = (By.XPATH, "//span[contains(.,'Delete')]")
    CONFIRM_DELETE_POPUP = (By.CSS_SELECTOR, 'body > div.p-confirm-popup.p-component.p-ripple-disabled')
    CONFIRM_DELETE_POPUP_BTN = (By.XPATH, "//button[contains(.,'Yes')]")
    EDIT_PET_AGE = (By.CSS_SELECTOR, "#age > input")
    EDIT_PET_SAVE_BTN = (By.CSS_SELECTOR, "#app > main > div > form > div > div.p-card-body > "
                                          "div.p-card-footer > button")

