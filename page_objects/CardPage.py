from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CardPage(BasePage):

    def go_smartphone_page(self):
        self.browser.find_element(By.LINK_TEXT, "iPhone").click()

    def thumbnail_items(self):
        thumbnail_items = self.browser.find_elements(By.CLASS_NAME, "thumbnail")
        if len(thumbnail_items) == 6:
            return True
        else:
            return "thumbnail_items !=6"

    def validate_elements(self):
        self.browser.find_element(By.CLASS_NAME, "product-thumb")
        self.browser.find_element(By.LINK_TEXT, "Description")
        self.browser.find_element(By.LINK_TEXT, "Reviews (0)")
        self.browser.find_element(By.CLASS_NAME, "btn-group")
        self.browser.find_element(By.ID, "button-cart")
        self.browser.find_elements(By.CLASS_NAME, "list-unstyled")
