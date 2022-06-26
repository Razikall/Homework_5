from selenium.webdriver.common.by import By
from Homework_5.page_objects.BasePage import BasePage
import allure


class CardPage(BasePage):
    iPhone_btn = (By.LINK_TEXT, "iPhone")
    THUMBNAIL = (By.CLASS_NAME, "thumbnail")
    PRODUCT_THUMB = (By.CLASS_NAME, "product-thumb")
    DESCRIPTION = (By.LINK_TEXT, "Description")
    REVIEWS = (By.LINK_TEXT, "Reviews (0)")
    BTNS_FUNC = (By.CLASS_NAME, "btn-group")
    BTN_CART = (By.ID, "button-cart")
    PRODUCT_INFO = (By.CLASS_NAME, "list-unstyled")

    @allure.step
    def go_smartphone_page(self):
        self.click(self.iPhone_btn)

    @allure.step
    def thumbnail_items(self):
        thumbnail_items = self.THUMBNAIL
        self.len_count(thumbnail_items, 6)

    @allure.step
    def validate_elements(self):
        self.log_element(self.PRODUCT_THUMB)
        self.log_element(self.DESCRIPTION)
        self.log_element(self.REVIEWS)
        self.log_element(self.BTNS_FUNC)
        self.log_element(self.BTN_CART)
        self.log_element(self.PRODUCT_INFO)
