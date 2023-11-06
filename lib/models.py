from sqlalchemy import create_engine
from sqlalchemy import UniqueConstraint, Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///mmg_properties.db')

Base = declarative_base()

class PropertyHost(Base):
    __tablename__ = 'property_hosts'
    __table_args__ = (
        UniqueConstraint('email', name='unique_email'),
        UniqueConstraint('contact',name='unique_contact')
    )

    id = Column(Integer, primary_key=True)
    name=Column(String)
    email = Column(String(25))
    gender=Column(String)
    contact = Column(Integer)
    
    def __repr__(self):
        return f"Host {self.id}, " + \
            f"name={self.name}, " + \
            f"contact = {self.contact}."
    

class Property (Base):
    __tablename__ = 'properties'
    __table_args__ = (
        UniqueConstraint('name', name='unique_name'),
    )

    id = Column(Integer, primary_key=True)
    name=Column(String)
    location = Column(String(20))
    price=Column(Integer)
    availability = Column(Boolean)
    host = relationship('PropertyHost', backref=backref('property', uselist=False))
    host_id=Column(Integer, ForeignKey('property_hosts.id'))
    reviews= relationship('Review', backref=backref('property'))

    def __repr__(self):
        return f"Property {self.id}, " + \
            f"name={self.name}, " + \
            f"price={self.price}. " 


class Review (Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    name=Column(String)
    rating = Column(Float)
    review = Column(String)
    property_id = Column(Integer, ForeignKey('properties.id'))
    
    
    def __repr__(self):
        return f"name= {self.name}, " + \
            f"rating={self.rating}, " + \
            f"review={self.review}. " 