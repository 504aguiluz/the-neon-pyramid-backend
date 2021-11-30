# imports
from flask import Flask, jsonify

# variables
DEBUG = True
PORT = 8000

# intializing an instance of Flask class
app = Flask(__name__)

# test routes
@app.route('/test')
def index():
    return '🍾 test route hit successfully 🍾'

@app.route('/test/json')
def neon():
    return jsonify(name="the neon pyramid", date_opened = 2749)

# run app
if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)