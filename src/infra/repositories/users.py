from sqlalchemy import delete, update
from sqlalchemy.orm import Session

from src.infra.config import DataBaseConnectionHandler
from src.infra.models.users import User
from src.infra.repositories.interface.i_users_repository import IUserRepository
from src.schemas.users import UserSchema


class UserRepository(IUserRepository):
    """
    This class represents the layer responsible for operations on the database.

    Params:
        IUserRepository (ABC): Apply the interface of UserRepository

    Attributes:
        database (session):
    """

    def __init__(self):
        self.database = Session(DataBaseConnectionHandler().get_engine())

    def create(self, data: UserSchema):
        """
        This method is responsible for creating new users

        Attributes:
            data (dict): Receives a dict with the data that will be created.

        Return:
        inserted_data (tuple): Returns a tuple with the created data.

        """
        try:
            new_user = User(name=data.name, password=data.password, email=data.email)
            self.database.add(new_user)
            self.database.commit()
            return new_user
        finally:
            self.database.refresh(new_user)

    def get_by_id(self, user_id: int) -> User:
        """
        This method is responsible for searching in the database an already existing user.

        Attributes:
            user_id (int): Receives a integer which represents the user id

        Returns:
            user_instance (User): Returns a User instance
        """
        try:
            user = self.database.query(User).filter(User.id == user_id).first()
            return user
        finally:
            self.database.close()

    def get_by_name(self, user_name: str) -> User:
        """
        This method is responsible for searching in the database an already existing user.

        Attributes:
            user_name (str): Receives a string which represents the user name

        Returns:
            user_instance (User): Returns a User instance
        """
        try:
            user_name = self.database.query(User).filter(User.name == user_name).all()
            return user_name
        finally:
            self.database.close()

    def get_by_email(self, email: str) -> User:
        """
        This method is responsible for searching an user by its email

        Attributes:
            email (str): Receives an
        """
        try:
            user = self.database.query(User).filter(User.email == email).first()
            return user
        finally:
            self.database.close()

    def partial_update(self, user_id: int, data: dict):
        """
        This method is responsible for updating tbe user

        Attributes:
            user_instance (User): Receives a User instance
            data (dict): Receives a dict with the data tha will be updated.

        Returns:
            user_instance (User): Returns a User instance
        """
        try:
            user = update(User).where(User.id == user_id).values(password=data.password)
            self.database.execute(user)
            self.database.commit()
            return user
        finally:
            self.database.close()

    def delete(self, user_id: int):
        """
        This method is responsible for deleting existing users.

        Attributes:
            user_id (int): Receives an int that represents the user's id
        """
        try:
            deleted_user = delete(User).where(User.id == user_id)
            self.database.execute(deleted_user)
            self.database.commit()
        finally:
            self.database.close()
