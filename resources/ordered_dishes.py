import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

# blueprint
ordered_dishes = Blueprint('ordered_dishes', 'ordered_dishes')

# index ordered_dishes -> /api/v1/ordered_dishes ======================================================
@ordered_dishes.route('/', methods = ['GET'])
def ordered_dishes_index():
    result = models.OrderedDish.select()
    print('')
    print('======== result of order select query ========')
    print(result)


    current_user_ordered_dish_dicts = [model_to_dict(ordered_dish) for ordered_dish in current_user.ordered_dishes]


    # for order_dict in current_user_ordered_dish_dicts:
    #     ordered_dishes_dict['order.customer'].pop('password')

    print('=====================================')
    return jsonify({
        'data': current_user_ordered_dish_dicts,
        'message': f'🧾 successfully found {len(current_user_ordered_dish_dicts)} ordered_dishes! 🧾',
        'status': 200
    }), 200


# create ordered_dish -> /api/v1/ordered_dishes/<order_id>/<dish_id>/ =====================================================
@ordered_dishes.route('/<order_id>/<dish_id>/', methods=['POST'])
# @login_required
def create_ordered_dish(order_id, dish_id):
    
    current_order = models.Order.get_by_id(order_id)
    current_dish = models.Dish.get_by_id(dish_id)
    
    print('here\'s the order to:', model_to_dict(current_order))
    print('here\'s the dish:', model_to_dict(current_dish))

    # if (dish is not in ordered_dishes):
        # create dish
    # else:
        # increment qtyOrdered by 1

    # sum of dish totals = ordered_dish.order.total

    new_ordered_dish = models.OrderedDish.create(qtyOrdered = 1, order=current_order, dish=current_dish, customer=current_user)
    
    new_ordered_dish_dict = model_to_dict(new_ordered_dish)

    print(f'this dish was ordered to order {current_order}: {new_ordered_dish_dict}')

    return jsonify (
        data = new_ordered_dish_dict,
        message = 'Successfully ordered a dish!',
        status = 200,
    ), 200

# delete ordered_dish -> /api/v1/ordered_dishes/<order_id>/<dish_id>/ =====================================================
@ordered_dishes.route('/<ordered_dish_id>/', methods=['DELETE'])
# @login_required
def delete_ordered_dish(ordered_dish_id):
    
    current_ordered_dish = models.OrderedDish.get_by_id(ordered_dish_id)

    current_ordered_dish_dict = model_to_dict(current_ordered_dish)

    delete_query = models.OrderedDish.delete().where(models.OrderedDish.id == ordered_dish_id)
    
    # print(current_ordered_dish_dict)
    print(f'here is the qtyOrdered:{current_ordered_dish.qtyOrdered}')
    # return current_ordered_dish_dict

    if (current_ordered_dish.qtyOrdered == 1):
        num_of_rows_deleted = delete_query.execute()
        print(f'num of rows deleted: {num_of_rows_deleted}')
        return jsonify(
            data = {},
            message =f'💣 Successfully deleted {num_of_rows_deleted} ordered dish with id {ordered_dish_id} 💣',
        status = 200
    ), 200
    else:
        print('ordered dish qty decremented by 1')
        current_ordered_dish.qtyOrdered -= 1
        print(f'here is the qtyOrdered:{current_ordered_dish.qtyOrdered}')
        return jsonify(
            data ={},
            message = f'ordered dish qty is now {current_ordered_dish.qtyOrdered}',
            status = 200
        ), 200

    # sum of dish totals = ordered_dish.order.total