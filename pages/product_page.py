import time
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        time.sleep(1)

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"

    def should_be_correct_product_name_in_success_message(self):
        product_name = self.get_product_name()
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert f"{product_name} has been added to your basket." == success_message, \
            f"Product name in message doesn't match. Expected: {product_name}, got: {success_message}"

    def should_be_basket_total_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), \
            "Basket total message is not presented"

    def should_be_correct_basket_total(self):
        product_price = self.get_product_price()
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert f"Your basket total is now {product_price}" == basket_total, \
            f"Basket total doesn't match product price. Expected: {product_price}, got: {basket_total}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*ProductPageLocators.CLICK_ON_BASKET)
        basket_link.click()
        return BasketPage(browser=self.browser, url=self.browser.current_url)

    def debug_page_elements(self):
        print("=== DEBUG PAGE ELEMENTS ===")

        try:
            product_name = self.get_product_name()
            print(f"Product name: {product_name}")
        except:
            print("Product name NOT FOUND")

        try:
            product_price = self.get_product_price()
            print(f"Product price: {product_price}")
        except:
            print("Product price NOT FOUND")

        try:
            add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
            print("Add to basket button: FOUND")
        except:
            print("Add to basket button: NOT FOUND")

        success_alerts = self.browser.find_elements(*ProductPageLocators.SUCCESS_ALERT)
        print(f"Success alerts found: {len(success_alerts)}")
        for i, alert in enumerate(success_alerts):
            print(f"Success alert {i + 1}: {alert.text}")

        info_alerts = self.browser.find_elements(*ProductPageLocators.INFO_ALERT)
        print(f"Info alerts found: {len(info_alerts)}")
        for i, alert in enumerate(info_alerts):
            print(f"Info alert {i + 1}: {alert.text}")

        print("=== END DEBUG ===")