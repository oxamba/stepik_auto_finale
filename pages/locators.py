from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    MAIN_LINK = "http://selenium1py.pythonanywhere.com/"


class LoginPageLocators:
    LOGIN_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_TEXT_FIELD = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTER_CONFIRM_PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BTN = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CONFIRMATION_ALERT = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")
    PRICE_ALERT = (By.CSS_SELECTOR, "#messages .alert-info p:nth-child(1)")


class BasketPageLocators:
    BASKET_HEADER = (By.CSS_SELECTOR, ".page-header")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
