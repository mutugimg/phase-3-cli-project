from faker import Faker
import random
from models import PropertyHost, Property, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///mmg_properties.db')

Session = sessionmaker(bind=engine)
session=Session()

fake = Faker()
session.query(PropertyHost).delete()
session.commit()

property_host_list= [
    PropertyHost(
       name=fake.name(),
       email=fake.email(),
       gender=random.choice(['M','F']),
       contact=fake.phone_number() 
    )
    for _ in range(20)
]

for host in property_host_list:
    session.add(host)
session.commit()

session.query(Property).delete()
session.commit()

properties = []
for host in property_host_list:
    property = Property(
       name=fake.company(),
       location=fake.address(),
       price=fake.random_int(min=3000, max=14000),
       availability=fake.boolean(),
       host_id = host.id
    )
    properties.append(property)
    session.add(property)
session.commit()


session.query(Review).delete()
session.commit()

for property in properties:
    rev =['Great place! Serene!', 'Kind host', 'Very clean', 'Will come back again for sure', 'Should improve on hygiene','Host is quite rude though']

    for _ in range(random.randint(0,3)):

        reviews= Review(
            name=fake.name(),
            rating=fake.random_int(min=3000, max=14000),
            review=random.choice(rev),
            property_id = property.id
        )
        session.add(reviews) 
    session.commit()   
    