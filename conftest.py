import datetime
import os
import pytest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.opera.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.1.31:8081")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("/Drivers"))
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--executor", action="store", default="192.168.1.31")


@pytest.fixture
def browser(request):
    # Сбор параметров запуска
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("==> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    if browser == "chrome":
        service = ChromiumService(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FFService(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        executor_url = f"http//{executor}:4444/wd/hub"
        caps = {
            "browserName": "chrome",
            "browserVersion": "101.0",
            "selenoid:options": {
                "enableVNC": False,
                "enableVideo": False
            },
            'goog:chromeOptions': {}
        }
        options = Options()
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps,
            options=options
        )

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser:{}".format(browser))

    def fin():
        driver.quit()
        logger.info("==> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    driver.maximize_window()
    request.addfinalizer(fin)

    driver.get(url)
    driver.url = url

    driver.implicitly_wait(5)

    return driver
