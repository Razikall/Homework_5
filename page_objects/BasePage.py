import logging
import allure
import selenium.common.exceptions
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser, wait=3):
        self.browser = browser
        self.wait = WebDriverWait(browser, wait)

        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.browser.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.browser.log_level)

    @allure.step
    def open(self, url):
        self.logger.info("Opening url: {}".format(self.browser.url))
        self.browser.get(url)

    @allure.step
    def click(self, locator):
        self.logger.info("Clicking element: {}".format(locator))
        try:
            return self.wait.until(EC.element_to_be_clickable(locator)).click()
        except selenium.common.exceptions.TimeoutException:
            allure.attach(
                name=f"{locator}",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Элемент {locator} не найден")

    @allure.step
    def log_element(self, locator):
        self.logger.info("Validate element: {}".format(locator))

    @allure.step
    def send_keys(self, locator, key):
        self.logger.info("Send key to input: {}".format(key))
        try:
            return self.wait.until(EC.element_to_be_clickable(locator)).send_keys(key)
        except selenium.common.exceptions.TimeoutException:
            allure.attach(
                name=f"{locator}",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Элемент {locator} не найден")

    @allure.step
    def len_count(self, locator, count):
        self.logger.info("Validate len element: {}".format(locator))
        if len(locator) == count:
            return True
        else:
            return "incorrect count"
