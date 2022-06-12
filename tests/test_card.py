from Homework_5.page_objects.CardPage import CardPage
from Homework_5.page_objects.MainPage import MainPage
from selenium.webdriver.common.by import By


def test_card_len_thumbnail(browser):
    CardPage(browser).go_smartphone_page()
    CardPage(browser).thumbnail_items()


def test_card_elements(browser):
    CardPage(browser).go_smartphone_page()
    CardPage(browser).validate_elements()
    browser.find_element(By.CLASS_NAME, "product-thumb")
    browser.find_element(By.LINK_TEXT, "Description")
    browser.find_element(By.LINK_TEXT, "Reviews (0)")
    browser.find_element(By.CLASS_NAME, "btn-group")
    browser.find_element(By.ID, "button-cart")
    browser.find_elements(By.CLASS_NAME, "list-unstyled")


def test_card_footer_blocks(browser):
    CardPage(browser).go_smartphone_page()
    MainPage(browser).footer_blocks()
