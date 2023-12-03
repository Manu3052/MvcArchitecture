from abc import ABC, abstractmethod
from dataclasses import dataclass

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.schemas.users import UserLogin, UserSchema

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


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

    def get_user_logged(token: str = Depends(oauth2_schema)):
        pass
