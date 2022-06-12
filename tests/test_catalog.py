from Homework_5.page_objects.CatalogPage import CatalogPage
from Homework_5.page_objects.MainPage import MainPage


def test_catalog_len_group_items(browser):
    CatalogPage(browser).go_catalog_page()
    CatalogPage(browser).catalog_page()


def test_catalog_len_featured_items(browser):
    CatalogPage(browser).go_catalog_page()
    MainPage(browser).feature_items()


def test_catalog_elements(browser):
    CatalogPage(browser).go_catalog_page()
    CatalogPage(browser).validate_elements()


def test_catalog_footer_blocks(browser):
    CatalogPage(browser).go_catalog_page()
    MainPage(browser).footer_blocks()
