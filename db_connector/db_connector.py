import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnector:
    def __init__(self):
        load_dotenv()
        self.DB_NAME = os.environ.get("DB_NAME")
        self.dsn = f'sqlite:///{self.DB_NAME}'
        self.engine = create_engine(self.get_dsn(), echo=False)
        self.Session = sessionmaker(bind=self.get_engine())

    def get_dsn(self):
        return self.dsn

    def get_engine(self):
        return self.engine

    def get_session(self):
        return self.Session


