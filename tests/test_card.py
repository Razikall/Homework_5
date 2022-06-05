def test_card_len_thumbnail(browser):
    browser.get(browser.url + "/smartphone/iphone")
    thumbnail_items = browser.find_elements_by_class_name("thumbnail")
    assert len(thumbnail_items) == 6


def test_card_elements(browser):
    browser.get(browser.url + "/smartphone/iphone")
    browser.find_element_by_class_name("product-thumb")
    browser.find_element_by_link_text("Description")
    browser.find_element_by_link_text("Reviews (0)")
    browser.find_element_by_class_name("btn-group")
    browser.find_element_by_id("button-cart")
    browser.find_elements_by_class_name("list-unstyled")


def test_card_footer_blocks(browser):
    browser.get(browser.url + "/smartphone/iphone")
    footer_blocks = browser.find_elements_by_xpath("//footer//ul")
    assert len(footer_blocks) == 4


def test_card_len_navbar(browser):
    browser.get(browser.url + "/smartphone/iphone")
    navbar_items = browser.find_elements_by_css_selector("ul.navbar-nav > li")
    assert len(navbar_items) == 8
