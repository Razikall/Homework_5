from Homework_5.page_objects.RegPage import RegPage


def test_reg(browser):
    RegPage(browser).find_reg_page()
    RegPage(browser).validate_elements()

    RegPage(browser).fill_personal("user", "lastuser", "312352")
    RegPage(browser).fill_password("qazqaz", "qazqaz")

    RegPage(browser).start_reg()
    RegPage(browser).validate_reg_message()
