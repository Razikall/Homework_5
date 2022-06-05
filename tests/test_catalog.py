def test_catalog_len_group_items(browser):
    browser.get(browser.url + "/smartphone")
    group_items = browser.find_elements_by_class_name("list-group-item")
    browser.find_elements_by_class_name("list-group-active-item")
    assert len(group_items) == 8


def test_catalog_len_featured_items(browser):
    browser.get(browser.url + "/smartphone")
    featured_items = browser.find_elements_by_class_name("product-thumb")
    assert len(featured_items) == 3


def test_catalog_elements(browser):
    browser.get(browser.url + "/smartphone")
    browser.find_element_by_id("compare-total")
    browser.find_element_by_class_name("btn-default")
    browser.find_element_by_class_name("input-group-addon")


def test_catalog_footer_blocks(browser):
    browser.get(browser.url + "/smartphone")
    footer_blocks = browser.find_elements_by_xpath("//footer//ul")
    assert len(footer_blocks) == 4


def test_catalog_len_navbar(browser):
    browser.get(browser.url + "/smartphone")
    navbar_items = browser.find_elements_by_css_selector("ul.navbar-nav > li")
    assert len(navbar_items) == 8
