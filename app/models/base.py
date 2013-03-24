#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from app.main import main

echo = not main.config['SQLALCHEMY_STFU']
engine = create_engine('sqlite:///%s' % main.config['APP_DB'], echo=echo, convert_unicode=True)

Session = scoped_session(sessionmaker(bind=engine))

class Model(object):
    def update(self):
        session = Session()
        session.merge(self)
        session.commit()

    def create(self):
        session = Session()
        session.add(self)
        session.commit()

Base = declarative_base(cls=Model)
