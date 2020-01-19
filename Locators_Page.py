from Base_Page import BasePage
from selenium.webdriver.common.by import By

class Locators:

    EMAIL_ID = (By.ID, "email")
    PASSWORD_ID = (By.ID, "passwd")
    AUTH_ID = (By.CLASS_NAME, "login")
    SIGN_ID = (By.ID, "SubmitLogin")
    ACCOUNT_ID = (By.CLASS_NAME, "account")


class SearchHelper(BasePage):

    def enter_word_email(self, word):
        search_field = self.find_element(Locators.EMAIL_ID)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def enter_word_pass(self, word):
        search_field = self.find_element(Locators.PASSWORD_ID)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_auth_button(self):
        return self.find_element(Locators.SIGN_ID,time=3).click()

    def check_error_message(self):
        all_list = self.find_elements(Locators.ACCOUNT_ID,time=3)
        nav_bar_menu = [x for x in all_list]
        return nav_bar_menu

    def click_sign_in_section(self):
        return self.find_element(Locators.AUTH_ID,time=3).click()