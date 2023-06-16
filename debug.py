#!/usr/bin/env python3
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Restaurant, Customer, Review
import ipdb

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///lib/db/restaurants.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()
