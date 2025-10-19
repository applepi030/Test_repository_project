import pytest
from pages.product_page import ProductPage



class TestUserAddToBasketFromProductPage:
    def test_guest_can_add_product_to_basket(self, browser):

        page=ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
        page.open()

        page.get_product_name()
        page.get_product_price()
        page.add_product_to_basket()
        page.should_be_success_message()
        page.should_be_correct_product_name_in_success_message()
        page.should_be_basket_total_message()
        page.should_be_correct_basket_total()


    def test_guest_cant_see_success_message_before_adding_product_to_basket(self, browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page=ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page=ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_disappear()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    basket = page.go_to_basket_page()
    basket.is_item_not_added_to_basket()
    basket.empty_basket_message()