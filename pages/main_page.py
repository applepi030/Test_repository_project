from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.locators import MainPageLocators, BasketPageLocators
from pages.login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert(self.is_element_present(*MainPageLocators.LOGIN_LINK)), 'Login link is not presented'

    def go_to_basket_page(self):
        basket_link=self.browser.find_element(*BasketPageLocators.BASKET_BTN)
        basket_link.click()
        return BasketPage(browser=self.browser, url=self.browser.current_url)

    def add_item_to_basket(self):
        add_button = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET)
        add_button.click()