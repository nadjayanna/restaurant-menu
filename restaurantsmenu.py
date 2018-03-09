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
@app.route('/restaurants/')
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('index.html', restaurants=restaurants)

@app.route('/restaurant/new/' , methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name = request.form['name'])
        session.add(newRestaurant)
        session.commit()
        flash("New Restaurant created!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('new_restaurant.html')

@app.route('/restaurant/<int:restaurant_id>/edit/' , methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            restaurant.name = request.form['name']
        session.add(restaurant)
        session.commit()
        flash("Restaurant edited!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('edit_restaurant.html', restaurant_id=restaurant_id, restaurant=restaurant)

@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurant)
        session.commit()
        flash("Restaurant Deleted!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('delete_restaurant.html', restaurant_id=restaurant_id, restaurant=restaurant)

@app.route('/courses')
def showCourses():
    courses = session.query(Course).all()
    return render_template('courses.html', courses=courses)

@app.route('/course/new', methods=['GET', 'POST'])
def newCourse():
    if request.method == 'POST':
        newCourse = Course(name = request.form['name'])
        session.add(newCourse)
        session.commit()
        flash("New Course created!")
        return redirect(url_for('showCourses'))
    else:
        return render_template('new_course.html')

@app.route('/course/<int:course_id>/edit' , methods=['GET', 'POST'])
def editCourse(course_id):
    course = session.query(Course).filter_by(id=course_id).one()
    if request.method == 'POST':
        if request.form['name']:
            course.name = request.form['name']
        session.add(course)
        session.commit()
        flash("Course edited!")
        return redirect(url_for('showCourses'))
    else:
        return render_template('edit_course.html', course_id=course_id, course=course)

@app.route('/course/<int:course_id>/delete', methods=['GET', 'POST'])
def deleteCourse(course_id):
    course = session.query(Course).filter_by(id=course_id).one()
    if request.method == 'POST':
        session.delete(course)
        session.commit()
        flash("Course Deleted!")
        return redirect(url_for('showCourses'))
    else:
        return render_template('delete_course.html', course_id=course_id, course=course)

@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    courses = session.query(Course).all()
    itensbycourse = []
    for course in courses:
        sublist = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, course_id=course.id).all();
        if sublist:
            itensbycourse.append((course,sublist))
    return render_template('menu.html', restaurant=restaurant, menu=itensbycourse)

@app.route('/restaurant/<int:restaurant_id>/menu/new/' , methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    courses = session.query(Course).all()
    
    if request.method == 'POST':
        newItem = MenuItem(name = request.form['name'], price=request.form['price'], description=request.form['description'], course_id = request.form['course'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("New MenuItem created!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('new_menuitem.html', restaurant_id=restaurant_id, restaurant=restaurant, courses=courses)


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

#Json Responce

@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])

@app.route('/courses/JSON')
def coursesJSON():
    courses = session.query(Course).all()
    return jsonify(Courses=[c.serialize for c in courses])

@app.route('/restaurants/JSON')
def restaurantsJSON():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants=[r.serialize for r in restaurants])

@app.route('/restaurant/<int:restaurant_id>/menu/<int:item_id>/JSON')
def restaurantMenuItemJSON(restaurant_id, item_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id, id=item_id).one()
    return jsonify(MenuItem=[items.serialize])

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run (host = '0.0.0.0', port = 5000)