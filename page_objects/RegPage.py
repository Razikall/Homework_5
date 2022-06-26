from selenium.webdriver.common.by import By
from Homework_5.helpers import random_email
from Homework_5.page_objects.BasePage import BasePage
import allure


class RegPage(BasePage):
    DROPDOWN = (By.CLASS_NAME, "dropdown")
    REG_PAGE_BTN = (By.LINK_TEXT, "Register")
    REGISTER_ACCOUNT = (By.LINK_TEXT, "Register Account")
    PERSONAL_DETAILS = (By.LINK_TEXT, "Your Personal Details")
    PASSWORD = (By.LINK_TEXT, "Your Password")
    NEWSLETTER = (By.LINK_TEXT, "Newsletter")
    FIRSTNAME = (By.ID, "input-firstname")
    LASTNAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")
    INPUT_PASSWORD = (By.ID, "input-password")
    INPUT_CONFIRM = (By.ID, "input-confirm")
    AGREE_BTN = (By.NAME, "agree")
    BTN_REG = (By.CLASS_NAME, "btn-primary")
    REG_MESSAGE = (By.ID, "content")

    @allure.step
    def find_reg_page(self):
        self.click(self.DROPDOWN)
        self.click(self.REG_PAGE_BTN)

    @allure.step
    def validate_elements(self):
        self.log_element(self.REGISTER_ACCOUNT)
        self.log_element(self.REGISTER_ACCOUNT)
        self.log_element(self.PERSONAL_DETAILS)
        self.log_element(self.PASSWORD)

    @allure.step
    def fill_personal(self):
        self.send_keys(self.FIRSTNAME, "user")
        self.send_keys(self.LASTNAME, "lastuser")
        self.send_keys(self.EMAIL, random_email())
        self.send_keys(self.TELEPHONE, "312352")

    @allure.step
    def fill_password(self):
        self.send_keys(self.INPUT_PASSWORD, "qazqaz")
        self.send_keys(self.INPUT_CONFIRM, "qazqaz")

    @allure.step
    def start_reg(self):
        self.click(self.AGREE_BTN)
        self.click(self.BTN_REG)

    @allure.step
    def validate_reg_message(self):
        self.log_element(self.REG_MESSAGE)
