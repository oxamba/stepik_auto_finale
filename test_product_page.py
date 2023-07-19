import pytest
from .pages.product_page import ProductPage

PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.parametrize("promo", [0, 1, 2, 3, 4, 5, 6, 8, 9, pytest.param(7, marks=pytest.mark.xfail(reason="some bug"))])
def test_guest_can_add_product_to_basket(browser, promo):
    promo_product_link = PRODUCT_LINK + "/?promo=offer" + str(promo)
    page = ProductPage(browser, promo_product_link)
    page.open()
    page.add_product()
    page.solve_quiz_and_get_code()
    page.should_be_confirmation_message()
    page.should_be_price_details()
