from Homework_5.page_objects.MainPage import MainPage


def test_main_len_navbar(browser):
    MainPage(browser).validate_navbar()


def test_main_len_featured_items(browser):
    MainPage(browser).feature_items()


def test_main_footer_blocks(browser):
    MainPage(browser).footer_blocks()


def test_main_open_catalog(browser):
    MainPage(browser).open_catalog()
    assert "Tablets" == browser.title


def test_change_currency(browser):
    MainPage(browser).change_currency()
