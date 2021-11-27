from faker import Faker

fake = Faker("Ru-ru")


class LoginData:
    """Методы для страницы логина."""

    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    @staticmethod
    def random():
        """
        Рандомизатор данных для логина.
        :return:
        """
        login = fake.email()
        password = fake.password()
        return LoginData(login=login, password=password)
