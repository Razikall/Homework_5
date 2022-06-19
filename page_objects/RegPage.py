from selenium.webdriver.common.by import By
from Homework_5.helpers import random_email
from .BasePage import BasePage


class RegPage(BasePage):

    def find_reg_page(self):
        self.browser.find_element(By.CLASS_NAME, "dropdown").click()
        self.browser.find_element(By.LINK_TEXT, "Register").click()

    def validate_elements(self):
        self.browser.find_elements(By.LINK_TEXT, "Register Account")
        self.browser.find_elements(By.LINK_TEXT, "Your Personal Details")
        self.browser.find_elements(By.LINK_TEXT, "Your Password")
        self.browser.find_elements(By.LINK_TEXT, "Newsletter")

    def fill_personal(self, firstname, lastname, telephone):
        self.browser.find_element(By.ID, "input-firstname").send_keys(firstname)
        self.browser.find_element(By.ID, "input-lastname").send_keys(lastname)
        self.browser.find_element(By.ID, "input-email").send_keys(random_email())
        self.browser.find_element(By.ID, "input-telephone").send_keys(telephone)

    def fill_password(self, pas, confirm):
        self.browser.find_element(By.ID, "input-password").send_keys(pas)
        self.browser.find_element(By.ID, "input-confirm").send_keys(confirm)

    def start_reg(self):
        self.browser.find_element(By.NAME, "agree").click()
        self.browser.find_element(By.CLASS_NAME, "btn-primary").click()

    def validate_reg_message(self):
        self.browser.find_element(By.ID, "content")
