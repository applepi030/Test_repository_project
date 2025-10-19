import pytest
import time
from pages.login_page import LoginPage
from pages.locators import BasePageLocators

class TestUserRegistration:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.email = str(time.time()) + "@fakemail.org"
        self.password = "TestPassword123"

    def test_user_can_register(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()

        login_page.register_new_user(self.email, self.password)
        assert login_page.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably user is not registered/logged in"