import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Property

engine = create_engine('sqlite:///mmg_properties.db')

Session = sessionmaker(bind=engine)
session = Session()

@click.command()

@click.option("--name", prompt="Enter name of property")
@click.option("--location", prompt="Where is the property located?")
@click.option("--price", prompt="Enter price of property")
@click.option("--availability", prompt="Is the property booked?")
@click.option("--host_id", prompt="Enter host ID")

def create_property(name,location,price,availability,host_id):
    add_property = Property(
        name=name,
        location=location,
        price=int(price),
        availability=bool(availability),
        host_id=int(host_id)
    )
    session.add(add_property)
    session.commit()

    click.echo(click.style(f"{name} is located in {location} for ${price}"))

create_property()



