from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, Course

engine = create_engine('sqlite:///restaurantsmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#course = session.query(Course).filter_by(name="Entree").one()
#course = session.query(MenuItem).filter_by(name="French Fries").one()
#course = session.query(Restaurant).filter_by(name="Urban Burger").one()
#session.delete(course)
#session.commit()


restaurant = session.query(Restaurant).filter_by(name="Urban Burger").one()
courses = session.query(Course).all()
itensbycourse = []
for course in courses:
	sublist = session.query(MenuItem).filter_by(restaurant_id=restaurant.id, course_id=course.id).all();
	print course.name
	if not sublist:
  		print "List is empty"
	else:
		itensbycourse.append((course,sublist))
		print "Add in List"

print "END FIRST FOR"

for itens in itensbycourse:
	print itens[0].name
	for item in itens[1]:
		print item.name;
	print "END SECOND FOR"
print "END THIRD FOR"

		
	