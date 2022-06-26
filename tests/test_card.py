from Homework_5.page_objects.CardPage import CardPage
from Homework_5.page_objects.MainPage import MainPage
import allure


@allure.title("Checking thumbnail items")
def test_card_len_thumbnail(browser):
    page = CardPage(browser)
    page.open(browser.url)
    page.go_smartphone_page()
    page.thumbnail_items()


@allure.title("Checking card items")
def test_card_elements(browser):
    page = CardPage(browser)
    page.open(browser.url)
    page.go_smartphone_page()
    page.validate_elements()


@allure.title("Checking footer blocks")
def test_card_footer_blocks(browser):
    page = CardPage(browser)
    page.open(browser.url)
    page.go_smartphone_page()
    MainPage(browser).footer_blocks()
