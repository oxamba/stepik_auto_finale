from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Basket substring is not a part of the current url"

    def should_be_basket_header(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HEADER), "Basket header is not presented"

    def should_be_empty_basket_message(self):
        expected_message = "Your basket is empty."
        actual_message = BasketPageLocators.EMPTY_BASKET_TEXT.text.strip()
        assert expected_message == actual_message, f"{expected_message} was expected, {actual_message} got instead"

    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Product is in the basket, but should not be"
