
from models import PropertyHost, Property, Review
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///mmg_properties.db')
Session = sessionmaker(bind=engine)
session=Session()

# Display all properties
def get_properties():
    properties = session.query(Property).all()
    for property in properties:
        click.echo(click.style((property),fg="green"))
# get_properties()


# Remove property
def remove_property(property_name):
    unavailable_property = session.query(Property).filter(Property.name == property_name).first()

    if unavailable_property:
        session.delete(unavailable_property)
        session.commit()
        click.echo(click.style(("Property deleted successfully"),fg="green"))

    else: 
        print('Invalid property name')
    











