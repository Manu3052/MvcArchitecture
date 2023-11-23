from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.infra.models.users import User


@dataclass
class IUserRepository(ABC):
    """
    This class is an interface that works as interface for the class UserRepository.

    An interface contains the params and rules that a certain method must follow to work properly.

    Attribute:
        ABC (abstract base classes): The interface Inherits all the methods and attributes of this class.
    """

    @abstractmethod
    def create(self, data: dict) -> tuple:
        """
        This method is an interface for the create.

        This method is responsible for creating users.

        Attributes:
            data (dict): Receives a dictionary with the data which will be created.

        Returns:
            inserted_data (tuple): Returns a tuple with the data created.
        """
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        """
        This method is an interface for the get_by_id.

        This method is responsible for searching in the database an already existing user.

        Attributes:
            user_id (int): Receives a integer which represents the user id

        Returns:
            user_instance (User): Returns a User instance
        """
        pass

    @abstractmethod
    def partial_update(self, user_instance: User, data: dict):
        """
        This method is an interface for the partial_update.

        This method is responsible for updating an existing user.

        Attributes:
            user_instance (User): Receives an instance from User
            data (dict): Receives a dict with that data that will be updated

        Returns:
            user_instance (User): Returns a User instance
        """
        pass

    @abstractmethod
    def delete(self, user_instance: User):
        """
        This method is an interface for the delete.

        This method is responsible for deleting existing users.

        Attributes:
            user_instance (User): Receives an instance from User
        """
        pass
