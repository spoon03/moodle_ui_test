class TestLogin:
    def test_login_with_valid_data(self, app):
        """
        Steps:
        1. Open login page
        2. Auth with valid data
        3. Check result
        """
        app.open_login_page()
        app.login.auth("name", "Password")
        assert 1 == 1  # TODO add assert
