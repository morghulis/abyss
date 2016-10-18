# -*- coding:utf-8 -*-
from sqlalchemy import __version__
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class SQLAlchemy_agent(object):
    def __init__(self, dburi, echo=False):
        self.engine = create_engine(dburi, echo=echo)
        self.model = declarative_base()
        self.session_factory = sessionmaker(bind=self.engine)

    @staticmethod
    def get_version():
        return __version__

    def create_all(self):
        self.model.metadata.create_all(bind=self.engine)

    def drop_all(self):
        self.model.metadata.drop_all(bind=self.engine)

    def new_session(self):
        return self.session_factory()

