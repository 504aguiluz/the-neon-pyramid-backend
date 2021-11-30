# imports
from flask import Flask, jsonify, g
import models

# variables
DEBUG = True
PORT = 8000

# intializing an instance of Flask class
app = Flask(__name__)

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

@app.route('/test')
def index():
    return '🍾 test route hit successfully 🍾'

@app.route('/test/json')
def neon():
    return jsonify(name="the neon pyramid", date_opened = 2749)

# run app
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)