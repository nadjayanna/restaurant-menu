from flask import Flask , render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

##import CRUD Operations##
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem, Course

##Create session and connect do DB##
engine = create_engine('sqlite:///restaurantsmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    output ="<html><body><h1>teste</h1>"
    for restaurant in restaurants:
        output+=restaurant.name
        output+="</br>"
    output +="</body></html>"
    return output

@app.route('/restaurant/new')
def newRestaurant():
    output = "<html><body><h1>Create New Restaurant</h1></body></html>"
    return output

@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    output = "<html><body><h1>Edit "
    output += restaurant.name
    output += "</h1></body></html>"
    return output

@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    output = "<html><body><h1>Delete "
    output += restaurant.name
    output += "</h1></body></html>"
    return output

@app.route('/courses')
def showCourses():
    courses = session.query(Course).all()
    output ="<html><body><h1>teste</h1>"
    for course in courses:
        output+=course.name
        output+="</br>"
    output +="</body></html>"
    return output

@app.route('/course/new')
def newCourse():
    output = "<html><body><h1>Create New Course</h1></body></html>"
    return output

@app.route('/course/<int:course_id>/')
@app.route('/course/<int:course_id>/edit')
def editCourse(course_id):
    course = session.query(Course).filter_by(id=course_id).one()
    output = "<html><body><h1>Edit "
    output += course.name
    output += "</h1></body></html>"
    return output

@app.route('/course/<int:course_id>/delete')
def deleteCourse(course_id):
    course = session.query(Course).filter_by(id=course_id).one()
    output = "<html><body><h1>Delete "
    output += course.name
    output += "</h1></body></html>"
    return output

@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    menu = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    output = "<html><body><h1>"
    output += restaurant.name
    output += "</h1>"
    for item in menu:
        output += item.name
        output += "</br>"
    output += "</body></html>"
    return output

@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
    output = "<html><body><h1>Create New Menu Item</h1></body></html>"
    return output

@app.route('/restaurant/<int:restaurant_id>/menu/<int:item_id>/edit')
def editMenuItem(restaurant_id, item_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    item = session.query(MenuItem).filter_by(id=item_id).one()
    output = "<html><body><h1>Edit "
    output += item.name
    output += " in "
    output += restaurant.name
    output += "</h1></body></html>"
    return output

@app.route('/restaurant/<int:restaurant_id>/menu/<int:item_id>/delete')
def deleteMenuItem(restaurant_id, item_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    item = session.query(MenuItem).filter_by(id=item_id).one()
    output = "<html><body><h1>Delete "
    output += item.name
    output += " in "
    output += restaurant.name
    output += "</h1></body></html>"
    return output


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run (host = '0.0.0.0', port = 5000)