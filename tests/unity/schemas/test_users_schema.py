import random

import pytest
from pydantic import ValidationError

from src.schemas.users import CreateUserSchema, UserLogin, UserSchema, UserUpdateSchema


class TestUsersSchema:
    """
    This class is responsible for testing all user schemas
    """

    def test_create_user_schema(self):
        """
        This method is responsible for testing the schema CreateUserSchema
        """
        user_created = CreateUserSchema(
            name="Jhon Doe", password="Abacadabra", email="jhon.doe@gmail.com"
        )
        assert user_created.name == "Jhon Doe"
        assert user_created.password == "Abacadabra"
        assert user_created.email == "jhon.doe@gmail.com"

    def test_create_user_schema_with_wrong_email(self):
        """
        This method is responsible for testing the schema CreateUserSchema
        """
        with pytest.raises(ValidationError):
            user_created = CreateUserSchema(
                name="Jhon Doe", password="Abacadabra", email="jhon.doe.gmail.com"
            )

    def test_user_schema(self):
        """
        This method is responsible for testing the schema UserSchema
        """
        user = UserSchema(
            id=random.randint(10000, 199999),
            name="Jhon Doe",
            email="jhon.doe@gmail.com",
        )
        assert user.name == "Jhon Doe"
        assert user.email == "jhon.doe@gmail.com"

    def test_user_update_schema(self):
        """
        This method is responsible for testing the schema UserUpdateSchema
        """
        user = UserUpdateSchema(password="Abacadabra")
        assert user.password == "Abacadabra"

    def test_user_login(self):
        """
        This method is responsible for testing the schema UserLogin
        """
        user = UserLogin(email="jhon.doe@gmail.com", password="Abacadabra")
        assert user.email == "jhon.doe@gmail.com"
        assert user.password == "Abacadabra"
