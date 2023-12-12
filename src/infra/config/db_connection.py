from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class DataBaseConnectionHandler:
    """
    Class responsible for handling the database connection

    Attributes:
        connection_string (str): Receives a string representing the database engine
        session (sessionmaker()): Receives a session of the database
    """

    def __init__(self):
        """ """
        self.__connection_string = config("SQL_ENGINE")
        self.session = None

    def get_engine(self):
        """
        This method is responsible for creating the engine

        Return:
            engine (): Returns the created engine
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        """
        This method is responsible for opening an sqlalchmey session

        Return:
            session (sessionmaker()): Receives a session of the database
        """
        db_connection = self.get_engine()
        session_maker = sessionmaker()
        self.session = session_maker(bind=db_connection)
        return self.session
