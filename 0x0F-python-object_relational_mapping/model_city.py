#!/usr/bin/python3
"""
Python script that defines the City class.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
	"""
	City class that inherits from Base.
	Attributes:
    	id (int): The id of the city.
    	name (str): The name of the city.
	state_id (int): The id of the state to which the city belongs.
	"""
	__tablename__ = "cities"
	id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	name = Column(String(128), nullable=False)
	state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

