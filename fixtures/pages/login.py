import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from fixtures.models.login import LoginData
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class LoginPage(BasePage):
    def _password_input(self) -> WebElement:
        return self.custom_find_element((By.ID, "password"))

    def _login_input(self) -> WebElement:
        return self.custom_find_element((By.ID, "username"))

    def _submit_button(self) -> WebElement:
        return self.custom_find_element((By.ID, "loginbtn"))

    def auth(self, data: LoginData, is_submit: bool = True):
        """
        Auth func
        Если мы не login  → login
        Если мы login → logout → login
        """
        logger.info(f"Login with user {data.login} and password {data.password}")
        self._login_input().send_keys(data.login)
        self._password_input().send_keys(data.password)
        if is_submit:
            self._submit_button().click()
