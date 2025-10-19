from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def is_item_added_to_basket(self):
        assert (self.is_element_present(*BasketPageLocators.ITEMS)), 'items is presented'

    def is_item_not_added_to_basket(self):
        assert (self.is_not_element_present(*BasketPageLocators.ITEMS)), 'items is NOT presented'

    def empty_basket_message(self):
        assert (self.is_element_present(*BasketPageLocators.EMPTY_BASKET)), 'empty basket'