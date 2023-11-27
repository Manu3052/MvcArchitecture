from dataclasses import dataclass

import sqlalchemy
from fastapi import APIRouter, HTTPException, Response, status

from src.infra.config.db_connection import DataBaseConnectionHandler
from src.infra.models.users import User
from src.infra.repositories.users import UserRepository
from src.routers.interface.i_users import IUserRouters
from src.schemas.users import CreateUserSchema, UserSchema, UserUpdateSchema

router = APIRouter()


@dataclass
class UserRouters(IUserRouters):
    """
    This class implements all the users routers.

    Params;
        IUserRouters (Interface): Implements all the methods and rules that must be followed.
    """

    @router.post(
        "/users", status_code=status.HTTP_201_CREATED, response_model=UserSchema
    )
    def create(user: CreateUserSchema):
        user_create = UserRepository().create(user)
        if not isinstance(user_create, User):
            HTTPException(
                detail="Não foi possivel criar um usuário.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return user_create

    @router.get(
        "/users/name", status_code=status.HTTP_200_OK, response_model=list[UserSchema]
    )
    def search_by_name(user_name: str):
        user = UserRepository().get_by_name(user_name)
        if len(user) <= 0:
            HTTPException(
                detail="Não foi encontrado nenhum usuário.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return user

    @router.get("/users/id", status_code=status.HTTP_200_OK, response_model=UserSchema)
    def search_by_id(user_id: int):
        user = UserRepository().get_by_id(user_id)
        if not isinstance(user, User):
            HTTPException(
                detail="Não foi encontrado nenhum usuário.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return user

    @router.patch("/users", status_code=status.HTTP_200_OK)
    def partial_update(user_id: int, data: UserUpdateSchema):
        user_updated = UserRepository().partial_update(user_id, data)
        if not isinstance(user_updated, sqlalchemy.sql.dml.Update):
            HTTPException(
                detail="Não foi possível atualizar o usuário",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return user_updated

    @router.delete("/users", status_code=status.HTTP_200_OK)
    def delete(delete_user_id: int):
        user_deleted = UserRepository().delete(delete_user_id)
        return user_deleted