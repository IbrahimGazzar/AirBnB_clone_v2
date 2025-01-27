#!/usr/bin/python3
"""
City Class:
    Inherits from BaseModel and Base
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import environ


class City(BaseModel, Base):
    """
    Represents Cities available to users
    """
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    else:
        name = ""
        state_id = ""
