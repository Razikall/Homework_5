from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CatalogPage(BasePage):

    def go_catalog_page(self):
        self.browser.find_element(By.LINK_TEXT, "Phones & PDAs").click()

    def catalog_page(self):
        group_items = self.browser.find_elements(By.CLASS_NAME, "list-group-item")
        if len(group_items) == 8:
            return True
        else:
            return "bfbfb"

    def validate_elements(self):
        self.browser.find_element(By.ID, "compare-total")
        self.browser.find_element(By.CLASS_NAME, "btn-default")
        self.browser.find_element(By.CLASS_NAME, "input-group-addon")