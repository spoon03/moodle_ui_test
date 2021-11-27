from selenium.webdriver.common.by import By


class LoginLocators:
    """Класс для описания локаторов страницы Login"""

    LOGIN_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginbtn")
    LOGIN_MENU = (By.ID, "action-menu-toggle-1")
    LOGIN_ERROR = (By.ID, "loginerrormessage")
