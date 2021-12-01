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
    payment_info = {
        "cc_num": CharField(unique = True),
        "cc_exp": CharField(),
        "cc_sec_code": CharField()
    }

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

    class Meta:
        database = DATABASE

# ===================================================
class Order(Model):
    created_at = DateTimeField(default = datetime.datetime.now)
    total = FloatField()
    customer = ForeignKeyField(User, backref='orders')
    # dishes = ForeignKeyField(Dish, backref='orders')

    class Meta:
        database = DATABASE
 
# ===================================================
class DishOrder(Model):
    dish = ForeignKeyField(Dish)
    order = ForeignKeyField(Order)

    class Meta:
        database = DATABASE

# ===================================================
# ===================================================

# initialize
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Order, Dish], safe = True)
    print('🤖 Connect to the DB and created tables if they don\'t already exist 🤖')
    DATABASE.close()