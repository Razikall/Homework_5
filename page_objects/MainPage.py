from selenium.webdriver.common.by import By
from Homework_5.page_objects.BasePage import BasePage
import allure


class MainPage(BasePage):
    NAVBAR_ITEM = (By.CSS_SELECTOR, "ul.navbar-nav > li")
    PRODUCT_THUMB = (By.CLASS_NAME, "product-thumb")
    FOOTER_BLOCKS = (By.XPATH, "//footer//ul")
    TABLET_BTN = (By.LINK_TEXT, "Tablets")
    TABLET_PAGE = (By.LINK_TEXT, "Tablets (1)")
    DROPDOWN_CUR = (By.CLASS_NAME, "dropdown-toggle")

    @allure.step
    def validate_navbar(self):
        navbar_items = self.NAVBAR_ITEM
        self.len_count(navbar_items, 8)

    @allure.step
    def feature_items(self):
        featured_items = self.PRODUCT_THUMB
        self.len_count(featured_items, 4)

    @allure.step
    def footer_blocks(self):
        footer_blocks = self.FOOTER_BLOCKS
        self.len_count(footer_blocks, 4)

    @allure.step
    def open_catalog(self):
        tablet_btn = self.TABLET_BTN
        self.click(tablet_btn)
        self.log_element(self.TABLET_PAGE)
