from dataclasses import dataclass

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from src.infra.providers.auth_provider import create_access_token, verify_access_token
from src.infra.providers.hash_provider import verify_hash
from src.infra.repositories.users import UserRepository
from src.middlewares.auth_middleware import AuthenticationMiddleware
from src.routers.interface.i_auth import IAuthRouters
from src.schemas.users import AccessToken, UserLogin, UserSchema

router = APIRouter()
oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


@dataclass
class AuthRouters(IAuthRouters):
    """
    This class implements the tokens routers.

    Params:
        IAuthRouters (interface): Implements the interface
    """

    @router.post(
        "/auth/token", status_code=status.HTTP_200_OK, response_model=AccessToken
    )
    def login(user: UserLogin):
        """
        This method is responsible for login-in the user

        Params:
            user (UserLogin): This params

        Return:
            (AccessToken) : Returns the schema with the data necessary
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

        token = create_access_token({"sub": user.email})

        return AccessToken(id=user.id, email=user.email, access=token)

    @router.get(
        "/auth/verify-user", status_code=status.HTTP_200_OK, response_model=UserSchema
    )
    def get_user_logged(token: str = Depends(oauth2_schema)):
        try:
            email = AuthenticationMiddleware().verify_token(token)
            if not email:
                raise HTTPException(
                    detail="Token inválido", status_code=status.HTTP_401_UNAUTHORIZED
                )
            user = UserRepository().get_by_email(email)
            if not user:
                raise HTTPException(
                    detail="Token inválido", status_code=status.HTTP_401_UNAUTHORIZED
                )
            return user
        except JWTError as error:
            raise HTTPException(
                detail="Token inválido", status_code=status.HTTP_401_UNAUTHORIZED
            )

    @router.get("/profile", response_model=UserSchema)
    def get_profile(user: UserLogin = Depends(get_user_logged)):
        return user
