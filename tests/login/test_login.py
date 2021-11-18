import pytest

from fixtures.models.login import LoginData


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
        assert 1 == 1  # TODO add assert

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
        assert 1 == 1  # TODO add assert

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_login_with_password(self, app, user_data, field):
        """
        Steps:
        1. Open login page
        2. Auth with invalid data
        3. Check result
        """
        # app.open_login_page()
        # setattr(user_data, field, None)
        # getattr(user_data, field)
        # data = LoginData(login=user_data.login, password=None)
        # app.login.auth(data)
        assert 1 == 1  # TODO add assert
