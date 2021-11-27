import logging

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


from fixtures.models.login import LoginData
from fixtures.pages.application import Application

logger = logging.getLogger("moodle")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://qacoursemoodle.innopolis.university/login/index.php",
        help="Moodle url",
    ),
    parser.addoption(
        "--username", action="store", default="super_qa_2021", help="username",
    ),
    parser.addoption(
        "--password", action="store", default="Password11!", help="Password",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="enter 'true' if you want run tests in headless mode of browser,\n"
        "enter 'false' - if not",
    ),


@pytest.fixture(scope="session")
def user_data(request):
    user = request.config.getoption("--username")
    password = request.config.getoption("--password")
    return LoginData(user, password)


@pytest.fixture()
def app(request):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")

    # Опции  драйвера
    chrome_options = Options()
    if headless == "false":
        chrome_options.headless = False
    else:
        chrome_options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    logger.info(f"Start app on {url}")
    app = Application(driver, url)
    yield app
    app.quit()
