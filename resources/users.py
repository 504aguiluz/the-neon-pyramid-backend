# imports
import models
from flask import Blueprint, request, jsonify
from flask_login import login_user, current_user, logout_user
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict


# blueprint
users = Blueprint('users', 'users')

# test -> /api/v1/users =============================================================
@users.route('/', methods=['GET'])
def test_user_resource():
    return "🏆 user resource works 🏆"

# register -> /api/v1/users/register =================================================
@users.route('/register', methods=['POST'])
def register():
    payload = request.get_json()

    payload['username'] = payload['username'].lower()
    payload['email'] = payload['email'].lower()
    payload['address'] = payload['address'].lower()
    payload['password'] = payload['password'].lower()

    print(payload)

    try:
        models.User.get(models.User.email == payload['email'])

        return jsonify(
            data = {},
            message=f"A user with {payload['email']} already exists!",
            status=401
        ), 401

    except models.DoesNotExist:

        pw_hash = generate_password_hash(payload['password'])

        created_user = models.User.create(
            username = payload['username'],
            email = payload['email'],
            phone_num = payload['phone_num'],
            address = payload['address'],
            password = pw_hash,
            payment_info = payload['payment_info']
        )

        login_user(created_user)

        created_user_dict = model_to_dict(created_user)

        print(created_user_dict)
        created_user_dict.pop('password')

        return jsonify(
            data = created_user_dict,
            message = f"🥇 Successfully registered user {created_user_dict['email']}! 🥇",
            statue = 201
        ), 201

# login -> /api/v1/users/login =======================================================
@users.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    payload['username'] = payload['username'].lower()
    payload['email'] = payload['email'].lower()

    try:
        user = models.User.get(models.User.email == payload['email'])
        user_dict = model_to_dict(user)
        password_is_good = check_password_hash(user_dict['password'], payload['password'])

        if(password_is_good):
            login_user(user)
            print(f"{current_user.username} is current_user.name in POST login")
            user_dict.pop('password')

            return jsonify(
                data = user_dict,
                message = f"Successfully logged in {user_dict['email']}!",
                status = 200
            ), 200
        else:
            print("email is no good")
            return jsonify(
                data = {},
                message = 'Email or password is incorrect', 
                status = 401
            ), 401

    except models.DoesNotExist:
        print('email not found')
        return jsonify(
            data = {},
            message = "Email or password is incorrect",
            status = 401
        ), 401

# logged_in_user -> /api/v1/users/logged_in_user =====================================
@users.route('/logged_in_user', methods=['GET'])
def get_logged_in_user():
    print(current_user)

    if not current_user.is_authenticated:
        return jsonify(
            data = {},
            message = 'No user is currently logged in',
            status = 401
        ), 401
    else: 
        print(f"{current_user.username} is current_user.name in GET logged_in_user")
        user_dict = model_to_dict(current_user)
        user_dict.pop('password')

        return jsonify(
            data = user_dict,
            message = f"🐬 Currently logged in as {user_dict['email']}. 🐬",
            status = 200
            ), 200


# logout -> /api/v1/users/logout =====================================================
@users.route('/logout', methods = ['GET'])
def logout():
    logout_user()
    return jsonify(
        data = {},
        message = "🌴 Successfully logged out 🌴",
        status = 200
    ), 200