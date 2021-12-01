# imports
import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required


# blueprint
dishes = Blueprint('dishes', 'dishes')

# index dishes -> /api/v1/dishes ======================================================
@dishes.route('/', methods=['GET'])
def dishes_index():
    try:
        dishes = [model_to_dict(dish) for dish in models.Dish.select()]
        print(dishes)

        return jsonify(
            data = dishes,
            status = {
                "code": 200,
                "message": "🍱  Successfuly indexed dishes! 🍱"
            }
        )

    except models.DoesNotExist:
        return jsonify(
            data = {},
            status = {
                "code": 401,
                "message": "Error: not getting resources!"
            }
        )


# create dish -> /api/v1/dishes ======================================================
@dishes.route('/', methods=['POST'])
def create_dishes():
    payload = request.get_json()
    print(type(payload), 'payload')
    dish = models.Dish.create(**payload)
    # viewing model as dict
    print('============= created this dish:')
    print(model_to_dict(dish), 'model to dict')
    print('================================')
    dish_dict = model_to_dict(dish)

    return jsonify(
        data = dish_dict,
        status = {
            "code": 201,
            "message": "🥘 Successfully created a new dish! 🥘"
        }
    )

# show dish -> /api/v1/dishes/<dish_id> =============================================
@dishes.route('/<id>', methods=['GET'])
def get_one_dish(id):
    dish = models.Dish.get_by_id(id)
    print(dish)

    return jsonify(
        data = model_to_dict(dish),
        status = {
            "code": 200,
            "message": "🍙 Successfully fetched a dish! 🍙",
        }
    ), 200

# update dish -> /api/v1/dishes/<dish_id> =============================================
@dishes.route('/<id>', methods=['PUT'])
def update_dog(id):
    payload = request.get_json()
    models.Dish.update(**payload).where(models.Dish.id == id).execute()

    return jsonify(
        data = model_to_dict(models.Dish.get_by_id(id)),
        status = {
            "code": 200,
            "message": '🧂 dish updated successfully! 🧂'
        }
    ), 200

# delete dish -> /api/v1/dishes/<dish_id>
@dishes.route('/<id>', methods=['DELETE'])
def delete_dog(id):
    delete_query = models.Dish.delete().where(models.Dish.id == id)
    num_of_rows_deleted = delete_query.execute()

    print(num_of_rows_deleted)

    if (num_of_rows_deleted == 0):
        print('💩 Nothing was deleted! 💩')
    else:
        return jsonify(
            data = {},
            message = f'💣 Successfully deleted {num_of_rows_deleted} order with id {id} 💣',
        status = 200
    ), 200