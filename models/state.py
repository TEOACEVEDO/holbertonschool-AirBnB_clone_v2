#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
import models
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="delete"
        )

    @property
    def cities(self):
        """
        Returns the list of City instances with
        state_id equals to the current State.id
        """
        list_c = list()
        cities = models.storage.all(City).values()

        for city in cities:
            if city.state_id == self.id:
                list_c.append(city)

        return (list_c)
