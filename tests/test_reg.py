def test_reg_footer_blocks(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    footer_blocks = browser.find_elements_by_xpath("//footer//ul")
    assert len(footer_blocks) == 4


def test_reg_len_navbar(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    navbar_items = browser.find_elements_by_css_selector("ul.navbar-nav > li")
    assert len(navbar_items) == 8


def test_reg_len_group(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    group_items = browser.find_elements_by_class_name("list-group-item")
    assert len(group_items) == 13


def test_reg_elements(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    browser.find_elements_by_link_text("Register Account")
    browser.find_elements_by_link_text("Your Personal Details")
    browser.find_elements_by_link_text("Your Password")
    browser.find_elements_by_link_text("Newsletter")
    browser.find_element_by_id("input-firstname")
    browser.find_element_by_id("input-lastname")
    browser.find_element_by_id("input-email")
    browser.find_element_by_id("input-telephone")
    browser.find_element_by_id("input-password")
    browser.find_element_by_id("input-confirm")
    browser.find_element_by_class_name("btn-primary")

