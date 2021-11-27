from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Класс с описанием базовых методов."""

    def __init__(self, app):
        self.app = app

    def custom_find_element(self, locator, wait_time=60) -> WebElement:
        """
        Поиск элемента по локатору
        :param locator:
        :param wait_time:
        :return:
        """
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def click_element(self, locator, wait_time=60) -> None:
        """
        click_element = click
        """
        element = self.custom_find_element(locator, wait_time)
        element.click()

    def fill_element(self, data, locator, wait_time=60) -> None:
        """
        Fill element (fill_element == send_keys)
        :param data: string to fill
        """
        element = self.custom_find_element(locator, wait_time)
        if data:
            element.send_keys(data)

    def get_text(self, locator, wait_time=60) -> str:
        """
        Get element text
        """
        element = self.custom_find_element(locator, wait_time)
        return element.text
