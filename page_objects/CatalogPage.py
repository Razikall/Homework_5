from selenium.webdriver.common.by import By
from Homework_5.page_objects.BasePage import BasePage
import allure


class CatalogPage(BasePage):
    TAB_BNT = (By.LINK_TEXT, "Phones & PDAs")
    TAB_ITEMS = (By.CLASS_NAME, "list-group-item")
    COMPARE_BTN = (By.ID, "compare-total")
    BTN_VIEW = (By.CLASS_NAME, "btn-default")
    SORT_BTN = (By.CLASS_NAME, "input-group-addon")

    @allure.step
    def go_catalog_page(self):
        self.click(self.TAB_BNT)

    @allure.step
    def catalog_page(self):
        group_items = self.TAB_ITEMS
        self.len_count(group_items, 8)

    @allure.step
    def validate_elements(self):
        self.log_element(self.COMPARE_BTN)
        self.log_element(self.BTN_VIEW)
        self.log_element(self.SORT_BTN)
