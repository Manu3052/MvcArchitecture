from sqlalchemy import Column, Integer, String

from src.infra.config.db_connection import Base


class User(Base):
    """
    Class representing the model for the table users.

    Params:
        Base (declarative_base()): Inherits a function that will mirror tbe model in a table

    Attributes:
        id (Integer, primary_key=True, autoincrement=True): Represents the primary key
        name (String, nullable=False): Represents the name of the User
        password (String, nullable=False): Represents the password for accessing the software
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(
        String,
        nullable=False,
    )
    password = Column(
        String,
        nullable=False,
    )
