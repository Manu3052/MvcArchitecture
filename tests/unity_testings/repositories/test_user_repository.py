import pytest
from sqlalchemy import text

from src.infra.config import DataBaseConnectionHandler
from src.infra.repositories.users import UserRepository
from src.schemas.users import CreateUserSchema, UserUpdateSchema

user_repository = UserRepository()
db_connection_handler = DataBaseConnectionHandler()


@pytest.mark.test_runs_all_repository_user_tests
class TestUserRepository:
    """
    This class is responsible for using unity tests to test the UserRepository class
    """

    def test_create_user(self):
        """
        This method tests the method create and it should be successful.
        """
        data = {"name": "Jonh Doe", "password": "Abracadabra"}
        data = CreateUserSchema(name=data["name"], password=data["password"])

        engine = db_connection_handler.get_engine().connect()
        new_user = user_repository.create(data)
        query_user = engine.execute(
            text(f"SELECT * FROM users us WHERE id={new_user.id}")
        ).fetchone()

        engine.execute(text(f"DELETE FROM users WHERE id={new_user.id}"))
        engine.commit()

        assert new_user.id == query_user.id
        assert new_user.name == query_user.name

    def test_get_existing_user_by_name(self):
        """
        Test the method is responsible for searching an existing user by its name
        """
        engine = db_connection_handler.get_engine().connect()
        mocked_name = "Jane Doe"
        mocked_password = "Password"
        sql = """
            INSERT INTO users (name, password) VALUES ('{}', '{}')
        """.format(
            mocked_name,
            mocked_password,
        )
        engine.execute(text(sql))
        engine.commit()

        response = user_repository.get_by_name(mocked_name)

        engine.execute(text(f"DELETE FROM users WHERE name='{mocked_name}'"))
        engine.commit()

        assert mocked_name == [item.name for item in response][0]
        assert type(response) is list

    def test_get_existing_user_by_id(self):
        """
        Test the method is responsible for searching an existing user by its id
        """
        engine = db_connection_handler.get_engine().connect()
        mocked_id = 90
        mocked_name = "Jane Doe"
        mocked_password = "Password"

        sql = """
            INSERT INTO users (id, name, password) VALUES ('{}','{}', '{}')
        """.format(
            mocked_id,
            mocked_name,
            mocked_password,
        )
        engine.execute(text(sql))
        engine.commit()

        response = user_repository.get_by_id(mocked_id)

        engine.execute(text(f"DELETE FROM users WHERE id='{mocked_id}'"))
        engine.commit()

        assert mocked_id == response.id
        assert mocked_password == response.password

    def test_updating_existing_user(self):
        """
        This method is responsible for updating an existing user
        """
        engine = db_connection_handler.get_engine().connect()
        mocked_name = "Jane Doe"
        mocked_password = "Password"

        sql = """
            INSERT INTO users (name, password) VALUES ('{}', '{}')
        """.format(
            mocked_name,
            mocked_password,
        )
        engine.execute(text(sql))
        engine.commit()

        user_instance = engine.execute(
            text(f"SELECT * FROM users WHERE name='{mocked_name}'")
        ).fetchone()

        data = UserUpdateSchema(password="Updated")

        user_repository.partial_update(user_instance.id, data)

        user_instance_updated = engine.execute(
            text(f"SELECT * FROM users WHERE name='{mocked_name}'")
        ).fetchone()

        engine.execute(text(f"DELETE FROM users WHERE id='{user_instance.id}'"))
        engine.commit()

        assert user_instance_updated.password == "Updated"

    def test_delete_user(self):
        """
        This method is responsible for testing the delete user
        """
        engine = db_connection_handler.get_engine().connect()
        mocked_name = "Jane Doe"
        mocked_password = "Password"

        sql = """
            INSERT INTO users (name, password) VALUES ('{}', '{}')
        """.format(
            mocked_name,
            mocked_password,
        )
        engine.execute(text(sql))
        engine.commit()

        user = engine.execute(
            text(f"SELECT * FROM users WHERE name='{mocked_name}'")
        ).fetchone()

        user_repository.delete(user.id)

        search_deleted_user = engine.execute(
            text(f"SELECT * FROM users WHERE id={user.id}")
        ).fetchone()

        assert search_deleted_user == None
