# imports
import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

# blueprint
dish_orders = Blueprint('dish_orders', 'dish_orders')

# index dish_order -> /api/v1/dish_orders ======================================================
@dish_orders.route('/', methods=['GET'])
def dish_orders_index():
    result = models.DishOrder.select()
    print('')
    print('======== result of dish_order select query ========')
    print(result)

    current_user_dish_orders_dicts = [model_to_dict(dish_order) for dish_order in current_user.dish_orders]

    # for order_dict in current_user_order_dicts:
    #     order_dict['customer'].pop('password')

    print('=====================================')
    return jsonify({
        'data': current_user_dish_orders_dicts,
        'message': f'🧾 successfully found {len(current_user_dish_orders_dicts)} dish_orders 🧾',
        'status': 200
    }), 200