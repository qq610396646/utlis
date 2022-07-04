from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib import parse


class Connection(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = parse.quote_plus(password)
        self.database = database
        self._engine = create_engine(f"mysql+pymysql://{self.user}:{self.password}@{self.host}:\
                {self.port}/{self.database}?charset=utf8mb4", echo=False)

    def connect(self):
        self.DBSession = sessionmaker(bind=self._engine)
        return self.DBSession

    @property
    def engine(self):
        return self._engine