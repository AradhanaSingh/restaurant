'''
This files sets up the database  using SQlAlchemy. 
Created restaurant and menu_item table.
Executing this file creates empty restaurantmenu.db in current directory
Using SQLAlchemy, creating a database is similar to creating objects in python
'''
# creating a database with SQl Alchemy has four major componenets
# configuration - imports all necessary module, sets all dependencies and binds code to SQLAlchemy engine
# class -- class code that we use to represent our data in python 
# table -- table that represents the specific tables in our database
# mapper -- that connects the column to the class it represents

# configuration at the beginning of the file
# module to manipulate different parts of the Python run-time environment
import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

# making instance if declarative_base class that we imported
# it will let SQLAlchemy know that our classes are special SQLAlchemy classes that correspond to table in pur database
# creates Base class that our class code will inherit
Base = declarative_base()

# class
# reprsentation of table as a python class, it extends Base class. 
# Nested inside will be table and mapper code
class Restaurant(Base):
    # representation of out table inside the database
	# table name
	__tablename__ = 'restaurant'
	
	# mappers
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)

class MenuItem(Base):
	# table name
	__tablename__ = 'menu_item'

	# mappers
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description =  Column(String(250))
	price = Column(String(8))
	course = Column(String(250))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    # we set relationship to Restaurant class
	restaurant = relationship(Restaurant)


# insert it at the end of the file
# creating instance of create_engine class and point to the database we will use
engine = create_engine('sqlite:///restaurantmenu.db')
# goes into the database and adds the classes we will created as new tables in our database
Base.metadata.create_all(engine)


