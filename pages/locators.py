from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = "login"
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > div")
    SUCCESS_MESSAGE_TEXT=(By.CSS_SELECTOR, ".alert-info.alertinner strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) > div > p")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alert-success.alertinner strong")
    SUCCESS_ALERT=(By.CSS_SELECTOR, ".alert-success")
    INFO_ALERT=(By.CSS_SELECTOR, ".alert-info")
    CLICK_ON_BASKET=(By.CSS_SELECTOR, ".basket-mini [href]")

class BasketPageLocators:
    ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini a.btn-default[href='/ru/basket/']")
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-primary")

