# imports
from flask import Flask, jsonify, g, after_this_request
import models
from resources.users import users
from resources.orders import orders
from resources.dishes import dishes
from resources.ordered_dishes import ordered_dishes
from flask_cors import CORS
from flask_login import LoginManager, login_manager
import os
from dotenv import load_dotenv

load_dotenv()

# variables
DEBUG = True
PORT = 8000

# intializing an instance of Flask class
app = Flask(__name__)

# LoginManager/cookies config
app.secret_key = os.environ.get("FLASK_APP_SECRET")
app.config['SESSION_COOKIE_SAMESITE'] = "None"
app.config['SESSION_COOKIE_SECURE'] = True
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    try:
        print('loading the following user')
        return models.User.get_by_id(user_id)
    except models.DoesNotExist:
        print('problem loading the following user...')
        return None

@login_manager.unauthorized_handler
def unauthorized():
    return jsonify(
        data = {
            'error': 'User not logged in'
        },
        message = 'You must be logged in to access that resource',
        status = 401
    ), 401

# CORS config
CORS(orders, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
CORS(dishes, origins=['http://localhost:3000'], supports_credentials=True)
CORS(ordered_dishes, origins=['http://localhost:3000'], supports_credentials=True)

# blueprint config
app.register_blueprint(orders, url_prefix='/api/v1/orders')
app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(dishes, url_prefix='/api/v1/dishes')
app.register_blueprint(ordered_dishes, url_prefix='/api/v1/ordered_dishes')

# app routes
# @app.before_request
# def before_request():
#     """Connect to the database before each request."""
#     g.db = models.DATABASE
#     g.db.connect()


# @app.after_request
# def after_request(response):
#     """Close the database connection after each request."""
#     g.db.close()
#     return response

@app.before_request 
def before_request():

    """Connect to the db before each request"""
    print("this before each request") 
    models.DATABASE.connect()

    @after_this_request 
    def after_request(response):
        """Close the db connetion after each request"""
        print("this after each request") 
        models.DATABASE.close()
        return response 

@app.route('/test')
def index():
    return '🍾 test route hit successfully 🍾'

@app.route('/test/json')
def neon():
    return jsonify(name="the neon pyramid", date_opened = 2749)

# initialize tables for heroku
if os.environ.get('FLASK_ENV') != 'development':
  print('\non heroku!')
  models.initialize()

# run app
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)