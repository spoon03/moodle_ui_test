from selenium.webdriver.common.by import By


class RegisterLocators:
    """Класс для описания локаторов страницы Регистрации."""

    LOGIN_INPUT = (By.ID, "id_username")
    PASSWORD_INPUT = (By.ID, "id_password")
    EMAIL_1 = (By.ID, "id_email")
    EMAIL_2 = (By.ID, "id_email2")
    NAME = (By.ID, "id_firstname")
    SURNAME = (By.ID, "id_lastname")
    CITY = (By.ID, "id_city")
    SUBMIT_BTN = (By.ID, "id_submitbutton")
    ERROR_FIRST_NAME = (By.ID, "id_error_firstname")
    PASS_REGISTER_TEXT = (By.CLASS_NAME, "errormessage")
    FAIL_REGISTER_TEXT = (By.CLASS_NAME, "fdescription")
