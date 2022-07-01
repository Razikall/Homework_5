from Homework_5.page_objects.ProductPage import ProductPage
import allure


@allure.title("Add product in admin")
def test_add_product(browser):
    page = ProductPage(browser)
    page.open(browser.url + "/admin")
    page.login()

    page.find_products_page()
    page.create_product()
    page.validate_message()


@allure.title("Delete product in admin")
def test_delete_product(browser):
    page = ProductPage(browser)
    page.open(browser.url + "/admin")
    page.login()

    page.find_products_page()
    page.find_product()

    page.delete_product()
    page.accept_alert()

    page.validate_message()
