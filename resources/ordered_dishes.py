import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

# blueprint
ordered_dishes = Blueprint('ordered_dishes', 'ordered_dishes')

# index ordered_dishes -> /api/v1/ordered_dishes ======================================================
@ordered_dishes.route('/', methods = ['GET'])
def ordered_dishes_index():

    current_user_ordered_dish_dicts = [model_to_dict(ordered_dish) for ordered_dish in current_user.ordered_dishes]


    for order_dict in current_user_ordered_dish_dicts:
        order_dict['customer'].pop('password')
        order_dict['order']['customer'].pop('password')
        print(order_dict)

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

    # queries what dishes an order has:
    # dishes = (models.Dish
    #         .select()
    #         .join(models.OrderedDish)
    #         .join(models.Order)
    #         .where(models.Order.id == current_order.id))
    
    # # queries ordered_dish containing current_order_id:
    # ordered_dishes = (models.OrderedDish
    #                     .select(models.OrderedDish, models.Dish, models.Order)
    #                     .join(models.Dish)
    #                     .switch(models.OrderedDish)
    #                     .join(models.Order)
    #                     .where(models.Order.id == current_order.id))

    # # make list of dicts
    # dishes_dict = [model_to_dict(dish) for dish in dishes]
    # ordered_dishes_dict = [model_to_dict(ordered_dish) for ordered_dish in ordered_dishes]


    new_ordered_dish = models.OrderedDish.create(qtyOrdered = 1, order=current_order, dish=current_dish, customer=current_user)

    print(f'{new_ordered_dish.dish.title} added to order {current_order}')
    new_ordered_dish_dict = model_to_dict(new_ordered_dish)


    new_ordered_dish_dict['customer'].pop('password')
    new_ordered_dish_dict['order']['customer'].pop('password')
    print(new_ordered_dish_dict)


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

    delete_query = models.OrderedDish.delete().where(models.OrderedDish.id == ordered_dish_id)
    
    print(f'{current_ordered_dish.dish.title} deleted from ordered dish with id: {ordered_dish_id}')
    
    num_of_rows_deleted = delete_query.execute()
    print(f'num of rows deleted: {num_of_rows_deleted}')

    return jsonify(
        data = {},
        message =f'💣 Successfully deleted {current_ordered_dish.dish.title} from ordered dish with id {ordered_dish_id} 💣',
    status = 200
    ), 200
    