from selenium.webdriver.common.by import By
from Homework_5.page_objects.BasePage import BasePage
import allure


class ProductPage(BasePage):
    USER_INPUT = (By.NAME, "username")
    PAS_INPUT = (By.NAME, "password")
    AUTH_BTN = (By.CLASS_NAME, "btn-primary")
    TAB_TYPE_LIST = (By.CLASS_NAME, "collapsed")
    FIND_TYPE = (By.XPATH, "//*[@id='collapse1']/li[2]/a")
    FILTER_INPUT = (By.ID, "input-name")
    FILTER_BTN = (By.ID, "button-filter")
    FILTER_PRODUCT = (By.NAME, "selected[]")
    BTN_ADD_PRODUCT = (By.CLASS_NAME, "btn-primary")
    NAME_INPUT = (By.ID, "input-name1")
    INPUT_META = (By.ID, "input-meta-title1")
    BTN_SWITCH = (By.XPATH, "//*[@id='form-product']/ul/li[2]/a")
    MODEL_INPUT = (By.NAME, "model")
    BTN_SAVE = (By.CLASS_NAME, "btn-primary")
    BTN_DELETE = (By.CLASS_NAME, "btn-danger")
    ALERT_MESSAGE = (By.CLASS_NAME, "alert-dismissible")

    @allure.step
    def login(self):
        self.send_keys(self.USER_INPUT, "user")
        self.send_keys(self.PAS_INPUT, "bitnami")
        self.click(self.AUTH_BTN)

    @allure.step
    def find_products_page(self):
        self.click(self.TAB_TYPE_LIST)
        self.click(self.FIND_TYPE)

    @allure.step
    def find_product(self):
        self.send_keys(self.FILTER_INPUT, "Product")
        self.click(self.FILTER_BTN)
        self.click(self.FILTER_PRODUCT)

    @allure.step
    def create_product(self):
        self.click(self.BTN_ADD_PRODUCT)
        self.send_keys(self.NAME_INPUT, "Product")
        self.send_keys(self.INPUT_META, "test")
        self.click(self.BTN_SWITCH)
        self.send_keys(self.MODEL_INPUT, "test1")
        self.click(self.BTN_SAVE)

    @allure.step
    def delete_product(self):
        self.click(self.BTN_DELETE)

    @allure.step
    def accept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    @allure.step
    def validate_message(self):
        self.log_element(self.ALERT_MESSAGE)
