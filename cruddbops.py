'''
To populate restaurantmenu.db database
'''

# resolve dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# importing classes 
from databasesetup import Restaurant, Base, MenuItem

# let program know which database engine we would like to communicate with
engine = create_engine('sqlite:///restaurantmenu.db')
# binding engine to the base class
# makes connection between class and tables within the database
Base.metadata.bind = engine

#established link of communication between code execution and engine we just created
DBSession = sessionmaker(bind = engine)

# SQLAlcehmy executes operations using an interface session
# Session allows us to write down all the commands we want to execute, but not send to the database until committed
# session gives you a staging zone for all the objects loaded into a database session object
session = DBSession()

# Adding restaurant
first_restaurant = Restaurant(name = "Urban Burger")
session.add(first_restaurant)
session.commit()
print "Added restaurant"

# find the table that corresponds to Restaurant class, get all data and return them in a list
session.query(Restaurant).all()

# Adding menu item
first_menuitem = MenuItem(name = "French Fries", description = "with garlic and parmesan", price = "$2.99", course = "Appetizer", restaurant = first_restaurant)

session.add(first_menuitem)
session.commit()
print "Added menuitem"

print "Name of first restaurant"
print session.query(Restaurant).first().name

print "All Restuarant's name"
restaurant_names = session.query(Restaurant).all()
for names in restaurant_names:
	print names.name

# to update an entry
restaurants = session.query(Restaurant).filter_by(name = 'Urban Burger')
print "Updating  name of restaurant from Urban Burger to Burger Palace"
for restaurant in  restaurants:
	# modified the name of restauarant
	restaurant.name = "Burger Place" 

	# add the object to the session
	session.add(restaurant)

	# commit the changes
	session.commit()
	
print "Finished updating"
# to delete an entry

restaurants = session.query(Restaurant).filter_by(name= 'Burger Place')
for restaurant in restaurants:
	print "Deleting " , restaurant.id
	session.delete(restaurant)
	session.commit()
    
