import logging

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from fixtures.models.login import LoginData
from fixtures.pages.application import Application

logger = logging.getLogger("moodle")
logger_api = logging.getLogger("api")


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


@pytest.fixture(scope="session")
def user_data(request):
    user = request.config.getoption("--username")
    password = request.config.getoption("--password")
    return LoginData(user, password)


@pytest.fixture()
def app(request):
    url = request.config.getoption("--url")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    logger.info(f"Start app on {url}")
    app = Application(driver, url)
    yield app
    app.quit()
