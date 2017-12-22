import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    menu_item = relationship('MenuItem', cascade = "delete")

class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column (String (30))
    menu_item = relationship('MenuItem', cascade = "delete")
        

class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course_id = Column(Integer, ForeignKey('course.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
####### insert at end of file #######

engine = create_engine('sqlite:///restaurantsmenu.db')
Base.metadata.create_all(engine)