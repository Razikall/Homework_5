from Homework_5.page_objects.CatalogPage import CatalogPage
from Homework_5.page_objects.MainPage import MainPage
import allure


@allure.title("Checking len group items")
def test_catalog_len_group_items(browser):
    page = CatalogPage(browser)
    page.open(browser.url)
    page.go_catalog_page()
    page.catalog_page()


@allure.title("Checking len featured items")
def test_catalog_len_featured_items(browser):
    page = CatalogPage(browser)
    page.open(browser.url)
    page.go_catalog_page()
    MainPage(browser).feature_items()


@allure.title("Checking catalog elements")
def test_catalog_elements(browser):
    page = CatalogPage(browser)
    page.open(browser.url)
    page.go_catalog_page()
    page.validate_elements()


@allure.title("Checking catalog footer blocks")
def test_catalog_footer_blocks(browser):
    page = CatalogPage(browser)
    page.open(browser.url)
    page.go_catalog_page()
    MainPage(browser).footer_blocks()
