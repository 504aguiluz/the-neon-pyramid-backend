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

# show ordered_dishes by <order_id>
# -> /api/v1/ordered_dishes/<order_id>/
@ordered_dishes.route('/<order_id>/', 
methods=['GET'])
# @login_required
def show_ordered_dishes_by_order_id(order_id):

    current_order = models.Order.get_by_id(order_id)
    # current_dish = models.Dish.get_by_id(dish_id)
    
    print('here\'s the order to:', model_to_dict(current_order))
    
    # queries ordered_dish containing current_order_id:
    ordered_dishes = (models.OrderedDish
                        .select(models.OrderedDish, models.Dish, models.Order)
                        .join(models.Dish)
                        .switch(models.OrderedDish)
                        .join(models.Order)
                        .where(models.Order.id == current_order.id))

    ordered_dishes_to_dict = [model_to_dict(ordered_dishes_by_order) for ordered_dishes_by_order in ordered_dishes]

    for od in ordered_dishes_to_dict:
        print('ordered_dish.order.id: ')
        print(od['order']['id'])

    return jsonify({
        'data': ordered_dishes_to_dict,
        'message': f'🧾 successfully found {len(ordered_dishes_to_dict)} ordered_dishes with order id: {current_order}! 🧾',
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


# update dup ordered_dishes -> /api/v1/ordered_dishes/<order_id>/<dish_id>/ =====================================================
@ordered_dishes.route('/<order_id>/<dish_id>/<ordered_dish_id>', methods=['PUT'])
# @login_required
def update_duplicate_ordered_dish(order_id, dish_id, ordered_dish_id):
    current_order = models.Order.get_by_id(order_id)
    current_dish = models.Dish.get_by_id(dish_id)
    current_ordered_dish = models.OrderedDish.get_by_id(ordered_dish_id)


    print('here\'s the current order id:', (current_order.id))
    print('here\'s the dish id:', (current_dish.id))


    # queries what dishes an order has:
    dishes = (models.Dish
            .select()
            .join(models.OrderedDish)
            .join(models.Order)
            .where(models.Order.id == current_order.id))
    
    # queries ordered_dish containing current_order_id:
    ordered_dishes = (models.OrderedDish
                        .select(models.OrderedDish, models.Dish, models.Order)
                        .join(models.Dish)
                        .switch(models.OrderedDish)
                        .join(models.Order)
                        .where(models.Order.id == current_order.id))

    # make list of dicts
    dishes_dict = [model_to_dict(dish) for dish in dishes]
    ordered_dishes_dict = [model_to_dict(ordered_dish) 
    for ordered_dish in ordered_dishes]
    current_ordered_dish_dict = model_to_dict(current_ordered_dish)

    for od in ordered_dishes:
        target = model_to_dict(od)
        # total order.total and all orderedDish.order.totals
        print(f'order total: {current_order.total}')
        current_order.total += current_ordered_dish_dict['dish']['price']
        print(f'new order total: {current_order.total}')
        print(f'ordererd_dish total: {od.order.total}')
        od.order.total += current_ordered_dish_dict['dish']['price']
        print(f'new ordererd_dish total: {od.order.total}')
        print()
        if target['dish']['id'] == current_dish.id:
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            print('target dish id:')
            print(target['id'])
            print('current ordered dish id:')
            print(current_ordered_dish_dict['id'])
            # announce duplicate
            print(f'ordered dish with id: {target} is a duplicate!')
            # increment current_ordered_dish__dict_qtyOrdered
            current_ordered_dish_dict['qtyOrdered'] += 1
            print('new current OD qtyOrdered:')
            # double current_ordered_dish__dict_price
            print(current_ordered_dish_dict['qtyOrdered'])
            current_ordered_dish_dict['dish']['price'] *= 2
            print('new current OD price:')
            print(current_ordered_dish_dict['dish']['price'])

            # delete target
            delete_query = models.OrderedDish.delete().where(models.OrderedDish.id == target['id'])
            num_of_rows_deleted = delete_query.execute()
            print(f'num of rows deleted: {num_of_rows_deleted}')
        else:
            print('====================================')
            print('target dish id:')
            print(target['dish']['id'])
            print('current ordered dish:')
            print(current_ordered_dish_dict['id'])
            print('not a duplicate')

    return jsonify(
        data = current_ordered_dish_dict,
        status = {
            "code": 200,
            "message": 'ordered dish updated successfully!'
        }
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
    