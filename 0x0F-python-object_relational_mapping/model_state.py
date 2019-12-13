#!/usr/bin/env python3
""" This module contains the class state"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ This clase is about state
        Attr:
        id(int): Th id of the state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
