import pytest
from fixtures.constants import RegisterConst
from fixtures.models.register import RegisterData


class TestRegistration:
    def test_registration_with_valid_data(self, app):
        """
        Steps:
        1. Open register page
        2. Add valid data
        3. Check result
        """
        app.open_register_page()
        data = RegisterData.random()
        app.register.add_new_user(data)
        assert app.register.get_pass_text() == RegisterConst.PASS_REGISTER

    @pytest.mark.parametrize(
        "field", ["login", "password", "email", "email_2", "name", "surname"]
    )
    def test_registration_with_empty_req_fields(self, app, field):
        """
        Steps:
        1. Open register page
        2. Add data with empty name
        3. Check result
        """
        app.open_register_page()
        data = RegisterData.random()
        setattr(data, field, None)
        app.register.add_new_user(data)
        assert app.register.get_fail_text() == RegisterConst.FAIL_REGISTER
