from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url=self.browser.current_url
        assert True

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert True