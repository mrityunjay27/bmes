from sqlalchemy.types import Enum
from datetime import datetime
from bmes.sharedbp import db
import enum
from flask_admin.contrib.sqla import ModelView

# Status
class GenderType(enum.Enum):
    Male='M'
    Female='F'
    Unknown='U'

customer_address = db.Table('customer_address',
    db.Column('customer_id', db.Integer, db.ForeignKey('customers.id'), primary_key=True),
    db.Column('address_id', db.Integer, db.ForeignKey('addresses.id'), primary_key=True)
)

# Base Model
class Base(db.Model):
     __abstract__ = True
     id = db.Column(db.Integer, primary_key=True)
     created_date = db.Column(db.DateTime(), default=datetime.now())
     modified_date = db.Column(db.DateTime(), default=datetime.now(), onupdate=datetime.now())
     is_deleted = db.Column(db.Boolean(), default=False)

# Person Model
class Person(Base):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name  = db.Column(db.String(50),nullable=True)
    last_name = db.Column(db.String(50))
    email_address  = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    gender  = db.Column('gender', Enum(GenderType))
    date_of_birth = db.Column(db.DateTime(), default=datetime.now())

# Customer Model
class Customer(Base):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer(), db.ForeignKey('people.id'), nullable=False)
    person = db.relationship('Person', backref=db.backref('person',cascade='all, delete-orphan',lazy=True))
    addresses = db.relationship('Address',secondary=customer_address,lazy='subquery')


class PersonAdmin(ModelView):
    column_list = ['first_name', 'last_name', 'email_address', 'phone_number', 'gender', 'date_of_birth']
    form_columns = ['first_name', 'middle_name', 'last_name', 'email_address', 'phone_number', 'gender', 'date_of_birth']
    column_filters = ['gender']
    column_searchable_list = ['first_name', 'last_name', 'email_address']

class CustomerAdmin(ModelView):
    column_list = ['id', 'person', 'addresses']
    form_columns = ['person', 'addresses']
    column_searchable_list = ['person.first_name', 'person.last_name']
    column_filters = ['addresses']

class AddressAdmin(ModelView):
    column_list = ['name', 'address_line_1', 'city', 'state', 'country', 'zip_code', 'address_type']
    form_columns = ['name', 'address_line_1', 'address_line_2', 'city', 'state', 'country', 'zip_code', 'address_type']
    column_filters = ['city', 'state', 'country', 'address_type']
    column_searchable_list = ['name', 'city', 'state', 'zip_code']

