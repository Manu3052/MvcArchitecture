from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class DataBaseConnectionHandler:
    """
    Class responsible for connecting database and api
    """

    def __init__(self):
        self.__connection_string = config("SQL_ENGINE")
        self.session = None

    def get_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def return_engine(self):
        return self.__connection_string

    def __enter__(self):
        db_connection = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=db_connection)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
