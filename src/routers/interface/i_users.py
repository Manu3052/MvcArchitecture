from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.schemas.users import CreateUserSchema, UserSchema, UserUpdateSchema


@dataclass
class IUserRouters(ABC):
    """
    This class is an interface for the class UserRouters which implements all the routers for user.
    """

    @abstractmethod
    def create(user: CreateUserSchema):
        pass

    @abstractmethod
    def search_by_name(user_name: str):
        pass

    @abstractmethod
    def search_by_id(user_id: int):
        pass

    @abstractmethod
    def partial_update(user_id: int, data: UserUpdateSchema):
        pass

    @abstractmethod
    def delete(delete_user_id: int):
        pass
