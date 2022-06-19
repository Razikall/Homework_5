from Homework_5.page_objects.ProductPage import ProductPage


def test_add_product(browser):
    browser.get(browser.url + "/admin")
    ProductPage(browser).login_data("user", "bitnami")

    ProductPage(browser).find_products_page()
    ProductPage(browser).create_product("Product", "test", "test1")
    ProductPage(browser).validate_message()


def test_delete_product(browser):
    browser.get(browser.url + "/admin")
    ProductPage(browser).login_data("user", "bitnami")

    ProductPage(browser).find_products_page()
    ProductPage(browser).find_product("Product")

    ProductPage(browser).delete_product()
    ProductPage(browser).accept_alert()

    ProductPage(browser).validate_message()
