from lib.models import Restaurant, Customer, Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///lib/db/restaurants.sqlite')
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Create instances of Restaurant
restaurant1 = Restaurant(name='Restaurant 1', price=3)
restaurant2 = Restaurant(name='Restaurant 2', price=2)
restaurant3 = Restaurant(name='Restaurant 3', price=4)

# Create instances of Customer
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')
customer3 = Customer(first_name='Michael', last_name='Johnson')

# Add the instances to the session
session.add_all([restaurant1, restaurant2, restaurant3, customer1, customer2, customer3])

# Commit the changes to the database
session.commit()

# Create instances of Review and establish relationships
review1 = Review(star_rating=4, restaurant_id=restaurant1.id,customer_id=customer1.id, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5,restaurant_id=restaurant2.id,customer_id=customer2.id, restaurant=restaurant2, customer=customer1)
review3 = Review(star_rating=3,restaurant_id=restaurant3.id,customer_id=customer3.id, restaurant=restaurant3, customer=customer2)
review4 = Review(star_rating=4,restaurant_id=restaurant1.id,customer_id=customer2.id, restaurant=restaurant1, customer=customer2)
review5 = Review(star_rating=2,restaurant_id=restaurant3.id,customer_id=customer1.id, restaurant=restaurant2, customer=customer3)

# Add the instances to the session
session.add_all([review1, review2, review3, review4, review5])

# Commit the changes to the database
session.commit()

# Close the session
session.close()
