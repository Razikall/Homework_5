def test_main_title_name(browser):
    browser.get(browser.url)
    assert "Your Store" == browser.title


def test_main_len_navbar(browser):
    navbar_items = browser.find_elements_by_css_selector("ul.navbar-nav > li")
    assert len(navbar_items) == 8


def test_main_len_featured_items(browser):
    featured_items = browser.find_elements_by_class_name("product-thumb")
    assert len(featured_items) == 4


def test_main_footer_blocks(browser):
    footer_blocks = browser.find_elements_by_xpath("//footer//ul")
    assert len(footer_blocks) == 4


def test_main_open_catalog_page(browser):
    tablet_btn = browser.find_element_by_link_text("Tablets")
    tablet_btn.click()
    browser.find_elements_by_link_text("Tablets (1)")
    assert "Tablets" == browser.title
