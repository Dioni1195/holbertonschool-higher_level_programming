#!/usr/bin/python3
""" This module contains the class state"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import text

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_mexico = session.query(State).filter_by(id=2).first()
    new_mexico.name = 'New Mexico'
    session.commit()
    session.close()
