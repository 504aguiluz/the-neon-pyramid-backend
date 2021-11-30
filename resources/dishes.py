# imports
import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required


# blueprint
dishes = Blueprint('dishes', 'dishes')