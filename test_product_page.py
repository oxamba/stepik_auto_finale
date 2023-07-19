from .pages.product_page import ProductPage


PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.add_product()
    page.solve_quiz_and_get_code()
    page.should_be_confirmation_message()
    page.should_be_price_details()


