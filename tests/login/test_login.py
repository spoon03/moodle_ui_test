import pytest
from selenium.webdriver.remote.webelement import WebElement
from fixtures.models.login import LoginData
from fixtures.locators.login import LoginLocators
from fixtures.constants import LoginConst


class TestLogin:
    def test_login_with_valid_data(self, app, user_data):
        """
        Steps:
        1. Open login page
        2. Auth with valid data
        3. Check result
        """
        app.open_login_page()
        app.login.auth(data=user_data, is_submit=True)
        assert type(app.login.custom_find_element(locator=LoginLocators.LOGIN_MENU, wait_time=10)) == WebElement

    def test_login_with_invalid_data(self, app):
        """
        Steps:
        1. Open login page
        2. Auth with invalid data
        3. Check result
        """
        app.open_login_page()
        data = LoginData.random()
        app.login.auth(data)
        assert app.login.get_alert_text() == LoginConst.ALERT_FAIL_LOGIN

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_login_with_password(self, app, field):
        """
        Steps:
        1. Open login page
        2. Auth with invalid data
        3. Check result
        """
        app.open_login_page()
        data = LoginData.random()
        setattr(data, field, None)
        data = LoginData(login=data.login, password=data.password)
        app.login.auth(data)
        assert app.login.get_alert_text() == LoginConst.ALERT_FAIL_LOGIN
