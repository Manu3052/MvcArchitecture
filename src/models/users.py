from pydantic import BaseModel


class User(BaseModel):
    """
    This class is a model for the table User

    Attributes:
        id (int): This camp is an int which represents the id
        name (str): This camp is a string which represents the name
        password (str): This camp is a string which represents the password
    """

    id: int
    name: str
    password: str
