from pages.main_page import MainPage

class VisibilityProducts:
    def test_guest_see_product_in_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
        page = MainPage(browser, link)
        page.open()
        page.add_item_to_basket()
        basket=page.go_to_basket_page()
        basket.is_item_added_to_basket()

    def test_guest_cant_see_product_in_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
        page = MainPage(browser, link)
        page.open()
        basket = page.go_to_basket_page()
        basket.is_item_not_added_to_basket()
        basket.empty_basket_message()
