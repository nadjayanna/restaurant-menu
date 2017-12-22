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

# Courses
session.add(Course(name="Not Specified"))
session.add(Course(name="Entree"))
session.add(Course(name="Appetizer"))
session.add(Course(name="Salads"))
session.add(Course(name="Soup"))
session.add(Course(name="Dessert"))
session.add(Course(name="Beverage"))
session.commit()

# Menu for UrbanBurger
restaurant = Restaurant(name="Urban Burger")
session.add(restaurant)
session.commit()

course = session.query(Course).filter_by(name="Entree").one()
session.add(MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce", price="$7.50", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",price="$5.50", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Sirloin Burger", description="Made with grade A beef", price="$7.99", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Grilled Cheese Sandwich", description="On Texas toast with American Cheese", price="$3.49", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Vegan Burger", description="Made with freshest of ingredients and home grown spices", price="$5.99", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Appetizer").one()
session.add(MenuItem(name="French Fries", description="with garlic and parmesan", price="$2.99", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Dessert").one()
session.add(MenuItem(name="Chocolate Cake", description="fresh baked and served with ice cream", price="$3.99", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Beverage").one()
session.add(MenuItem(name="Root Beer", description="16oz of refreshing goodness",price="$1.99", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Iced Tea", description="with Lemon",price="$.99", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

# Menu for Super Stir Fry
restaurant = Restaurant(name="Super Stir Fry")
session.add(restaurant)
session.commit()

course = session.query(Course).filter_by(name="Appetizer").one()
session.add(MenuItem(name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",price="$7.99", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Entree").one()
session.add(MenuItem(name="Peking Duck", description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price="$25", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",price="$15", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",price="$12", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Soup").one()
session.add(MenuItem(name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.", price="$14", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.", price="$12", course_id=course.id, restaurant_id=restaurant.id))
session.commit()


# Menu for Panda Garden
restaurant = Restaurant(name="Panda Garden")
session.add(restaurant)
session.commit()

course = session.query(Course).filter_by(name="Soup").one()
session.add(MenuItem(name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.", price="$8.99", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Appetizer").one()
session.add(MenuItem(name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",price="$6.99", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Entree").one()
session.add(MenuItem(name="Gyoza", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner",price="$9.95", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",price="$6.99", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce", price="$9.50", course_id=course.id, restaurant_id=restaurant.id))
session.commit()


# Menu for Thyme for that
restaurant = Restaurant(name="Thyme for That Vegetarian Cuisine ")
session.add(restaurant)
session.commit()

course = session.query(Course).filter_by(name="Dessert").one()
session.add(MenuItem(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",price="$2.99", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",price="$4.50", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Entree").one()
session.add(MenuItem(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",price="$5.99", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",price="$7.95", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce", price="$6.80", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Appetizer").one()
session.add(MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",price="$6.95", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

# Menu for Tony's Bistro
restaurant = Restaurant(name="Tony\'s Bistro ")
session.add(restaurant)
session.commit()

course = session.query(Course).filter_by(name="Entree").one()
session.add(MenuItem(name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",price="$13.95", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Chicken and Rice", description="Chicken... and rice", price="$4.95", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",price="$6.95", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg", price="$7.95", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Dessert").one()
session.add(MenuItem(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)", description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

# Menu for Andala's
restaurant = Restaurant(name="Andala\'s")
session.add(restaurant)
session.commit()

course = session.query(Course).filter_by(name="Entree").one()
session.add(MenuItem(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",price="$9.95", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",price="$7.95", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",price="$7.00", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Appetizer").one()
session.add(MenuItem(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",price="$6.50", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",price="$6.75", course_id=course.id, restaurant_id=restaurant.id))
session.commit()


# Menu for Auntie Ann's
restaurant = Restaurant(name="Auntie Ann\'s Diner ")
session.add(restaurant)
session.commit()

course = session.query(Course).filter_by(name="Entree").one()
session.add(MenuItem(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",price="$8.99", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast", price="$10.95", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",price="$8.95", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce", price="$9.50", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Dessert").one()
session.add(MenuItem(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness", price="$2.99", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",price="$1.99", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Appetizer").one()
session.add(MenuItem(name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter, served on herbed toast slices",price="$7.50", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

# Menu for Cocina Y Amor
restaurant = Restaurant(name="Cocina Y Amor ")
session.add(restaurant)
session.commit()

course = session.query(Course).filter_by(name="Entree").one()
session.add(MenuItem(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",price="$5.95", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",price="$7.99", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

# Menu for State Bird Provisions
restaurant = Restaurant(name="State Bird Provisions")
session.add(restaurant)
session.commit()

course = session.query(Course).filter_by(name="Appetizer").one()
session.add(MenuItem(name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",price="$5.95", course_id=course.id, restaurant_id=restaurant.id))
session.commit()

course = session.query(Course).filter_by(name="Dessert").one()
session.add(MenuItem(name="Guanciale Chawanmushi", description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",price="$6.95", course_id=course.id, restaurant_id=restaurant.id))
session.add(MenuItem(name="Lemon Curd Ice Cream Sandwich", description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",price="$4.25", course_id=course.id, restaurant_id=restaurant.id))
session.commit()


print "added menu items!"
