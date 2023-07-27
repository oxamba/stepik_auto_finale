from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_textfield = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_TEXT_FIELD)
        email_textfield.send_keys(email)
        password_textfield = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_TEXT_FIELD)
        password_textfield.send_keys(password)
        confirm_password_textfield = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_TEXT_FIELD)
        confirm_password_textfield.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "Login substring is not a part of the current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"
