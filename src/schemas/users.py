from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    """
    This class is a schema for the creation of users

    Attributes:
        name (str): This camp is a string which represents the name
        password (str): This camp is a string which represents the password
    """

    name: str
    password: str


class UserSchema(BaseModel):
    """
    This class is a schema for the users

    Attributes:
        id (int): This camp is an int which represents the id
        name (str): This camp is a string which represents the name
        password (str): This camp is a string which represents the password
    """

    id: int
    name: str
    password: str


class UserUpdateSchema(BaseModel):
    """
    This class is a schema for the users

    Attributes:
        password (str): This camp is a string which represents the password
    """

    password: str
