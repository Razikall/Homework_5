from selenium.webdriver.common.by import By
from .BasePage import BasePage


class ProductPage(BasePage):

    def login_data(self, username, password):
        self.browser.find_element(By.NAME, "username").send_keys(username)
        self.browser.find_element(By.NAME, "password").send_keys(password)
        self.browser.find_element(By.CLASS_NAME, "btn-primary").click()

    def find_products_page(self):
        self.browser.find_element(By.CLASS_NAME, "collapsed").click()
        self.browser.find_element(By.XPATH, "//*[@id='collapse1']/li[2]/a").click()

    def find_product(self, product):
        self.browser.find_element(By.ID, "input-name").send_keys(product)
        self.browser.find_element(By.ID, "button-filter").click()
        self.browser.find_element(By.NAME, "selected[]").click()

    def create_product(self, name, tag, model):
        self.browser.find_element(By.CLASS_NAME, "btn-primary").click()
        self.browser.find_element(By.ID, "input-name1").send_keys(name)
        self.browser.find_element(By.ID, "input-meta-title1").send_keys(tag)
        self.browser.find_element(By.XPATH, "//*[@id='form-product']/ul/li[2]/a").click()
        self.browser.find_element(By.NAME, "model").send_keys(model)
        self.browser.find_element(By.CLASS_NAME, "btn-primary").click()

    def delete_product(self):
        self.browser.find_element(By.CLASS_NAME, "btn-danger").click()

    def accept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def validate_message(self):
        self.browser.find_element(By.CLASS_NAME, "alert-dismissible")
