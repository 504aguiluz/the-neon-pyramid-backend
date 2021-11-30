# imports
from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('neon-pyramid.sqlite')

# models 
# ===================================================

class User(UserMixin, Model):
    username = CharField(unique = True)
    email = CharField(unique = True)
    phone_num = CharField(unique = True)
    address = CharField(unique = True)
    password = CharField(unique = True)
    # paymentInfo = {
    #     ccNum = CharField(unique = True)
    #     ccExp = DateTimeField([formats='%Y-%m-%d'])
    #     ccSecCode = CharField()
    # }

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
    title = CharField(unique = True)
    price = FloatField()
    image = CharField(unique = True)
    description = CharField(unique = True)
    category = CharField()
    labels = [CharField()]
    order = ForeignKeyField(Order, backref='dishes')

    class Meta:
        database = DATABASE

# ===================================================

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Order, Dish], safe = True)
    print('🤖 Connect to the DB and created tables if they don\'t already exist 🤖')
    DATABASE.close()