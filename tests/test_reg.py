from Homework_5.page_objects.RegPage import RegPage
import allure


@allure.title("Registration")
def test_reg(browser):
    page = RegPage(browser)
    page.open(browser.url)
    page.find_reg_page()
    page.validate_elements()

    page.fill_personal()
    page.fill_password()

    page.start_reg()
    page.validate_reg_message()
