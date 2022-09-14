import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer)

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine('sqlite:///restaurants.db', echo=True)

class Restaurants(Base):
    pass

class Review(Base):
    pass

class Customer(Base):
    pass


Base.metadata.create_all(bind=engine)
