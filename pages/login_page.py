from pages.base_page import BasePage
from pages.locators import LoginPageLocators, ProductPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url=self.browser.current_url

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password1_field=self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password1_field.send_keys(password)
        password2_field=self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password2_field.send_keys(password)
        register_button=self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def login_user(self, email, password):
        email_field=self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email_field.send_keys(email)
        password_field=self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        password_field.send_keys(password)
        login_button=self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
