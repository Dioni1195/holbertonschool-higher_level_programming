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
    stm = text("SELECT id FROM states WHERE name=:name")
    state = session.query(State).from_statement(stm).params(name=argv[4]).all()
    if len(state) is 0:
        print("Not found")
    else:
        print(state[0].id)
    session.close()
