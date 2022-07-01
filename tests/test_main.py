from Homework_5.page_objects.MainPage import MainPage
import allure


@allure.title("Checking items")
def test_main_len_navbar(browser):
    page = MainPage(browser)
    page.validate_navbar()
    page.feature_items()
    page.footer_blocks()
    page.open_catalog()
    assert "Tablets" == browser.title
