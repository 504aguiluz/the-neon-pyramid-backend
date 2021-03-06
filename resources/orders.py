# imports
import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

# blueprint
orders = Blueprint('orders', 'order')
# OrderDish = Blueprint('OrderDish', 'OrderDish')
# index order -> /api/v1/orders ======================================================
@orders.route('/', methods=['GET'])
def orders_index():
    result = models.Order.select()
    print('')
    print('======== result of order select query ========')
    print(result)

    current_user_order_dicts = [model_to_dict(order) for order in current_user.orders]

    # for order_dict in current_user_order_dicts:
    #     order_dict['customer'].pop('password')

    print('=====================================')
    return jsonify({
        'data': current_user_order_dicts,
        'message': f'๐งพ successfully found {len(current_user_order_dicts)} orders ๐งพ',
        'status': 200
    }), 200

# create order -> /api/v1/orders =====================================================
@orders.route('/', methods=['POST'])
# @login_required
def create_order():
    payload = request.get_json()
    print('here is my payload:')
    print(payload)
    print(current_user)
    print(current_user.id)
    new_order = models.Order.create(total=payload['total'], customer=current_user.id)
    order_dict = model_to_dict(new_order)
    # order_dict['customer'].pop('password')

    return jsonify(
        data = order_dict,
        message = '๐ successfully created order! ๐',
        status = 201
    ), 201

# show route -> api/v1/orders/<order_id> =============================================
@orders.route('/<id>', methods=['GET'])
# @login_required
def get_one_order(id):
    order = models.Order.get_by_id(id)
    print(order)

    return jsonify(
        data = model_to_dict(order),
        message = 'Success! Here\'s an order.',
        status = 200,
    ), 200

# add dish to order -> api/v1/orders/add_dish/<dish_id>/<order_id>===========================================
@orders.route('/add_dish/<dish_id>/<order_id>', methods=['PUT'])
# @login_required
def add_dish_to_order(dish_id, order_id):
    
    current_dish = models.Dish.get_by_id(dish_id)
    current_order = models.Order.get_by_id(order_id)

    print('here\'s the dish:', model_to_dict(current_dish))
    print('here\'s the order:', model_to_dict(current_order))
    
    try:
        current_order.dishes.add(current_dish)
    
    except models.IntegrityError as err:
        print('dish already present in order!')
        print('Error: ' + err)
        
    dishes = [model_to_dict(dish) for dish in current_order.dishes]
    print(dishes)
    return jsonify(
        data = dishes,
        message = '๐ You added a dish to your order! ๐',
        status = 200
    ), 200

# update route -> api/v1/orders/<order_id> ===========================================
@orders.route('/<id>', methods=['PUT'])
# @login_required
def update_order(id):
    payload = request.get_json()
    models.Order.update(**payload).where(models.Order.id == id).execute()

    return jsonify(
        data = model_to_dict(models.Order.get_by_id(id)),
        message = '๐งฌ order updated successfully ๐งฌ',
        status = 200
    ), 200

# delete route -> api/v1/orders/<order_id> ===========================================
@orders.route('/<id>', methods=['DELETE'])
def delete_order(id):
    delete_query = models.Order.delete().where(models.Order.id == id)
    num_of_rows_deleted = delete_query.execute()

    print(num_of_rows_deleted)

    if (num_of_rows_deleted == 0):
        print('๐ฉ Nothing was deleted! ๐ฉ')
    else:
        return jsonify(
            data = {},
            message = f'๐ฃ Successfully deleted {num_of_rows_deleted} order with id {id} ๐ฃ',
        status = 200
    ), 200


















@orders.route('/ordertest', methods=['GET'])
# @login_required
def order_test():
    # order = models.Order.get_by_id(2)

    order = models.OrderDish.select()
    orders = [model_to_dict(order_dish) for order_dish in order]
    print((orders))

    return jsonify(
        data = model_to_dict(order),
        message = 'Success! Here\'s an order.',
        status = 200,
    ), 200