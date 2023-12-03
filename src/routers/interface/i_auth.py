from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.schemas.users import UserLogin, UserSchema


@dataclass
class IAuthRouters(ABC):
    """
    This class is an interface for the class AuthRouters which implements the route to token verification.
    """

    def login(user: UserLogin):
        """
        This method is responsible for login-in the user

        Params:
            user (UserLogin): This params
        """
        pass
