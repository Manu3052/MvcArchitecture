from dataclasses import dataclass

import sqlalchemy
from fastapi import APIRouter, Depends, HTTPException, status

from src.infra.models.users import User
from src.infra.providers.hash_provider import hash_generate
from src.infra.repositories.interface.i_users_repository import IUserRepository
from src.infra.repositories.users import UserRepository
from src.routers.auth import AuthRouters
from src.routers.interface.i_auth import IAuthRouters
from src.routers.interface.i_users import IUserRouters
from src.schemas.users import CreateUserSchema, UserSchema, UserUpdateSchema

router = APIRouter()


@dataclass
class UserRouters(IUserRouters):
    """
    This class implements all the users routers.

    Params:
        IUserRouters (Interface): Implements all the methods and rules that must be followed.
    """

    @router.post(
        "/users", status_code=status.HTTP_201_CREATED, response_model=UserSchema
    )
    def create(user: CreateUserSchema):
        verify_email = UserRepository().get_by_email(user.email)
        if verify_email:
            raise HTTPException(
                detail="Esse email já foi cadastrado.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        user.password = hash_generate(user.password)
        user_create = UserRepository().create(user)
        if not isinstance(user_create, User):
            raise HTTPException(
                detail="Não foi possivel criar um usuário.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return user_create

    @router.get(
        "/users/", status_code=status.HTTP_200_OK, response_model=list[UserSchema]
    )
    def search_by_name(name: str):
        user = UserRepository().get_by_name(name)
        if len(user) <= 0:
            raise HTTPException(
                detail="Não foi encontrado nenhum usuário.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return user

    @router.get(
        "/users/{id}", status_code=status.HTTP_200_OK, response_model=UserSchema
    )
    def search_by_id(id: int):
        user = UserRepository().get_by_id(id)
        if not isinstance(user, User):
            raise HTTPException(
                detail="Não foi encontrado nenhum usuário.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return user

    @router.patch("/users", status_code=status.HTTP_200_OK)
    def partial_update(user_id: int, data: UserUpdateSchema):
        user_updated = UserRepository().partial_update(user_id, data)
        if not isinstance(user_updated, sqlalchemy.sql.dml.Update):
            raise HTTPException(
                detail="Não foi possível atualizar o usuário",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return user_updated

    @router.delete("/users", status_code=status.HTTP_200_OK)
    def delete(delete_user_id: int):
        user_deleted = UserRepository().delete(delete_user_id)
        return user_deleted
