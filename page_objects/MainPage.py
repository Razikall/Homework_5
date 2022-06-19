from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):

    def validate_navbar(self):
        navbar_items = self.browser.find_elements(By.CSS_SELECTOR, "ul.navbar-nav > li")
        if len(navbar_items) == 8:
            return True
        else:
            return "navbar items !=8"

    def feature_items(self):
        featured_items = self.browser.find_elements(By.CLASS_NAME, "product-thumb")
        if len(featured_items) == 4:
            return True
        else:
            return "featured items !=4"

    def footer_blocks(self):
        footer_blocks = self.browser.find_elements(By.XPATH, "//footer//ul")
        if len(footer_blocks) == 4:
            return True
        else:
            return "footer blocks !=4"

    def open_catalog(self):
        tablet_btn = self.browser.find_element(By.LINK_TEXT, "Tablets")
        tablet_btn.click()
        self.browser.find_elements(By.LINK_TEXT, "Tablets (1)")

    def change_currency(self):
        self.browser.find_element(By.CLASS_NAME, "dropdown-toggle").click()
        self.browser.find_element(By.NAME, "EUR").click()
        test4 = self.browser.find_element(By.ID, "cart-total").text
        if test4 == "0 item(s) - 0.00€":
            return True
        else:
            return "Incorrect currency"
