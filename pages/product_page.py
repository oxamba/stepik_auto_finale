from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_btn.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def is_success_message_disappeared(self):
        assert self.is_element_present(*ProductPageLocators.CONFIRMATION_ALERT)
        assert self.is_disappeared(*ProductPageLocators.CONFIRMATION_ALERT, timeout=10), \
            "Success message should disappear, but os still there"

    def should_be_confirmation_message(self):
        confirmation_alert = self.browser.find_element(*ProductPageLocators.CONFIRMATION_ALERT)
        text_from_confirmation_alert = confirmation_alert.text
        expected_name = self.get_product_name()
        assert expected_name == text_from_confirmation_alert, f"""Product name is absent/is different in the 
                                                              confirmation alert after product is added to the 
                                                              basket. Expected: '{expected_name}', The text from 
                                                              alert was: {text_from_confirmation_alert}"""

    def should_be_price_details(self):
        price_alert = self.browser.find_element(*ProductPageLocators.PRICE_ALERT)
        text_from_price_alert = price_alert.text
        expected_price = self.get_product_price()
        assert expected_price in text_from_price_alert, f"""Product price is absent/is different in the 
                                                            confirmation alert after product is added to the 
                                                            basket. Expected: '{expected_price}', The text from 
                                                            alert was: {text_from_price_alert}"""

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CONFIRMATION_ALERT), \
            "Success message is presented, but should not be"
