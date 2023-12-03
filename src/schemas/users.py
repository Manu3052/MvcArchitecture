from pydantic import BaseModel, EmailStr


class CreateUserSchema(BaseModel):
    """
    This class is a schema for the creation of users

    Attributes:
        name (str): This camp is a string which represents the name
        password (str): This camp is a string which represents the password
        email (EmailStr): This camp is the user email address
    """

    name: str
    password: str
    email: EmailStr


class UserSchema(BaseModel):
    """
    This class is a schema for the users

    Attributes:
        id (int): This camp is an int which represents the id
        name (str): This camp is a string which represents the name
        email (str): This camps is a string which the email
    """

    id: int
    name: str
    email: str


class UserUpdateSchema(BaseModel):
    """
    This class is a schema for the users

    Attributes:
        password (str): This camp is a string which represents the password
    """

    password: str


class UserLogin(BaseModel):
    """
    This class is a schema used for the user login

    Attributes:
        email (str): this camp is a string which represents the email
        password (str): this camp is a password which represents the password
    """

    email: str
    password: str
