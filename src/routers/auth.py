from dataclasses import dataclass

import sqlalchemy
from fastapi import APIRouter, HTTPException, Response, status

from src.infra.providers.hash_provider import verify_hash
from src.infra.repositories.users import UserRepository
from src.routers.interface.i_auth import IAuthRouters
from src.schemas.users import UserLogin, UserSchema

router = APIRouter()


@dataclass
class AuthRouters(IAuthRouters):
    """
    This class implements the tokens routers.

    Params:
        IAuthRouters (interface): Implements the interface
    """

    @router.post("/token", status_code=status.HTTP_200_OK, response_model=UserSchema)
    def login(user: UserLogin):
        """
        This method is responsible for login-in the user

        Params:
            user (UserLogin): This params
        """
        user_password = user.password
        user_email = user.email
        user = UserRepository().get_by_email(user_email)
        if not user:
            raise HTTPException(
                detail="Esse email não foi cadastrado.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        valid_password = verify_hash(user_password, user.password)
        if valid_password is not True:
            raise HTTPException(
                detail="Senha incorreta.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        return user
