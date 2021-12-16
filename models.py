# imports
import os
from playhouse.db_url import connect
from enum import unique
from flask.json import jsonify
from peewee import *
import datetime
from flask_login import UserMixin
from playhouse.sqlite_ext import *

DATABASE = connect(os.environ.get('DATABASE_URL') or 'sqlite:///neon-pyramid.sqlite')

# models 
# ===================================================
class User(UserMixin, Model):
    username = CharField(unique = True)
    email = CharField(unique = True)
    phone_num = CharField(unique = True)
    address = CharField(unique = True)
    password = CharField(unique = True)
    cc_num = CharField(),
    cc_exp =  CharField(),
    cc_sec_code = CharField(),

    class Meta:
        database = DATABASE

# ===================================================
class Order(Model):
    created_at = DateTimeField(default = datetime.datetime.now)
    total = FloatField()
    customer = ForeignKeyField(User, backref='orders')

    class Meta:
        database = DATABASE
 
# ===================================================
class Dish(Model):
    title = CharField()
    price = FloatField()
    image = CharField()
    description = CharField()
    category = CharField()
    # orders = ForeignKeyField(Order, backref='dishes', null=True, default=None)

    class Meta:
        database = DATABASE

# ===================================================

class OrderedDish(Model):

    qtyOrdered = IntegerField()
    customer = ForeignKeyField(User, backref='ordered_dishes')
    order = ForeignKeyField(Order, backref='ordered_dishes')
    dish = ForeignKeyField(Dish, backref='ordered_dishes')

    class Meta:
        database = DATABASE

# ===================================================
# initialize
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Order, Dish, OrderedDish], safe = True)
    print('🤖 Connect to the DB and created tables if they don\'t already exist 🤖')
    DATABASE.close()