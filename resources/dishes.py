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

# seed dish -> /api/v1/seed
@dishes.route('/seed', methods=['POST'])
def seed_dishes():

    payload_list = [
        
        # =============8 APPS =================
    {
    "category": "app",
    "description": "six nutrient-fortified dumplings: flavors based on the cuisine of each sector in Neo-saka.",
    "image": "https://i.imgur.com/wLIpX96m.png",
    "price": 25.75,
    "title": "nutrient dumplings", 
    },

    {
    "category": "app",
    "description": "printed pizza bites with faux-mozzarella, basil, marinara concentrate, locally-grown micro-prosciutto",
    "image": "https://i.imgur.com/06TfTimm.jpg",
    "price": 32.50,
    "title": "3D printed micro pizza", 
    },

    {
    "category": "app",
    "description": "artisinally spliced fungi-pierogis with bespoke umami flavoring and exclusively patented mushroom blends",
    "image": "https://i.imgur.com/H49qi2Vm.jpg",
    "price": 47.00,
    "title": "fungisphere pierogis", 
    },

    {
    "category": "app",
    "description": "locally raised micro-koi atop a bed of protein-rice",
    "image": "https://i.imgur.com/u7gDLK1m.jpg",
    "price": 28.50,
    "title": "micro-koi nigiri", 
    },

    {
    "category": "app",
    "description": "10 multi-course meal bites, all bespoke flavor patents: chicken parmesan, mac-n-cheese casserole, cilantro-labneh, pork-jigae, black-truffled roast pork, octopus stifado, grilled hitaki, chipotle sesame shrimp, horse borsch, tabbouleh cremé",
    "image": "https://i.imgur.com/W6n28qzm.jpg",
    "price": 55.75,
    "title": "nitro meal spheres", 
    },

    {
    "category": "app",
    "description": "freshly pilled salad ingredients. mix and match!",
    "image": "https://i.imgur.com/u8Vtyaym.jpg",
    "price": 30.25,
    "title": "salad pill bites", 
    },

    {
    "category": "app",
    "description": "perfectly balanced tomato basil soup dodecohedrons",
    "image": "https://i.imgur.com/7wGpLnwm.jpg?2",
    "price": 42.0,
    "title": "tomato basil soup dodecohedrons", 
    },

    {
    "category": "app",
    "description": "neo-mediterranean salad sprout tarts",
    "image": "https://i.imgur.com/xKOpIuKl.jpg",
    "price": 24.50,
    "title": "veggie salad tarts", 
    },

    # =============8 BEVS =================

    {
    "category": "bev",
    "description": "partially aerosolized cotton candy vodka tonic",
    "image": "https://i.imgur.com/tmE0C7Mm.png",
    "price": 20.0,
    "title": "cotton candy vodka tonic", 
    },

    {
    "category": "bev",
    "description": "old-world cuban rum and reconstituted micro-fruit blend with simply syrup",
    "image": "https://i.imgur.com/c2xc7XBm.jpg",
    "price": 24.00,
    "title": "fruitini", 
    },

    {
    "category": "bev",
    "description": "wide variety of beer flavored malt liquors",
    "image": "https://i.imgur.com/UDtgOl1m.jpg",
    "price": 14.50,
    "title": "happochu", 
    },

    {
    "category": "bev",
    "description": "luma take on an old classic gin and tonic",
    "image": "https://i.imgur.com/HwTB6bum.jpg",
    "price": 20.00,
    "title": "luma GnT", 
    },

    {
    "category": "bev",
    "description": "a neosaka classic: espresso, matcha and chipotle oil",
    "image": "https://i.imgur.com/ngzpE6Fm.jpg",
    "price": 12.75,
    "title": "neospresso", 
    },

    {
    "category": "bev",
    "description": "gelatinized portable coffee",
    "image": "https://i.imgur.com/qEPbJsum.png",
    "price": 11.50,
    "title": "portable coffee cubes", 
    },

    {
    "category": "bev",
    "description": "rum, tequila, dinoflagellate-infused mescalina, simple syrup, aromatics",
    "image": "https://i.imgur.com/8YrFz9Hm.jpg",
    "price": 52.75,
    "title": "the vortex", 
    },

    {
    "category": "bev",
    "description": "500ml gelatinized water modules",
    "image": "https://i.imgur.com/k7el2fPm.jpg",
    "price": 19.50,
    "title": "water", 
    },

    # =============7 DESSERTS=================

    {
    "category": "dessert",
    "description": "printed candied marzipan skulls. flavors include: chocolate walnut, bubblegum, fresh fruit",
    "image": "https://i.imgur.com/iTnXAgrm.jpg",
    "price": 28.50,
    "title": "3D printed candied marzipan skulls", 
    },

    {
    "category": "dessert",
    "description": "3D printed mini chocolate apple pies",
    "image": "https://i.imgur.com/cyju2GPm.png",
    "price": 35.00,
    "title": "mini chocolate apple pies", 
    },

    {
    "category": "dessert",
    "description": "layered dinoflagellate-infused glazed focaccia",
    "image": "https://i.imgur.com/JCrUXO6m.png",
    "price": 20.0,
    "title": "luma bread", 
    },

    {
    "category": "dessert",
    "description": "glazed donuts with dinoflagellate-infused icing. three to an order",
    "image": "https://i.imgur.com/XaCFREmm.jpg",
    "price": 26.50,
    "title": "luma donuts", 
    },

    {
    "category": "dessert",
    "description": "stack of 5 micro algae pancakes topped with syrup, whipped cream and freshly printed fruit",
    "image": "https://i.imgur.com/d6OdU5zm.jpg",
    "price": 32.0,
    "title": "microalgae pancakes", 
    },

    {
    "category": "dessert",
    "description": "combined dna from fish roe for structure and raspberries for flavor, we’ve created this unique dessert experience",
    "image": "https://i.imgur.com/VnONfF2m.jpg",
    "price": 49.50,
    "title": "reconstructed berry roe", 
    },

    {
    "category": "dessert",
    "description": "another unique experience: live pomegranate injected white chocolate torte",
    "image": "https://i.imgur.com/ez2XJ57m.jpg",
    "price": 0.0,
    "title": "reconstructed white pomegranate torte", 
    },

    # =============16 ENTREES=================

    {
    "category": "entree",
    "description": "citrus braised cicada salad with badlands sea-salt and post-peruvian pepper",
    "image": "https://i.imgur.com/ENkSPndm.jpg",
    "price": 63.00,
    "title": "braised cicada salad", 
    },

    {
    "category": "entree",
    "description": "cajun-boiled recombined crawlobster with braised spinach",
    "image": "https://i.imgur.com/Rq1jG0Um.jpg",
    "price": 67.50,
    "title": "crawlobster spinach bowl", 
    },

    {
    "category": "entree",
    "description": "a neosaka classic: cricket okonomiyaki",
    "image": "https://i.imgur.com/wu0JRoMm.jpg",
    "price": 59.75,
    "title": "cricket okonomiyaki", 
    },

    {
    "category": "entree",
    "description": "wild trychopeplus fortified with vitamin bundle and neurotropic enhancements. serves 2",
    "image": "https://i.imgur.com/J4WGuC0m.jpg",
    "price": 275.50,
    "title": "fortified wild trychopeplus", 
    },

    {
    "category": "entree",
    "description": "reconstituted turkey dinner, perfectly indocharged to temperature. *please specify if desired temp is other than medium.",
    "image":  "https://i.imgur.com/zjsFRM2m.jpg",
    "price": 73.00,
    "title": "indocharged turkey dinner", 
    },

    {
    "category": "entree",
    "description": "roasted squid filled dinoflagellate-infused crepes with algae sauce",
    "image": "https://i.imgur.com/XwM3tthm.jpg",
    "price": 68.75,
    "title": "lumabite squid crepes", 
    },

    {
    "category": "entree",
    "description": "dinoflagellate-infused sushi box: maguro, salmon, ebi",
    "image": "https://i.imgur.com/bPHIOSOm.jpg",
    "price": 75.00,
    "title": "lumabite sushi box", 
    },

    {
    "category": "entree",
    "description": "tamago pho with bok chow, carrot and mushroom rings. served with a side of berry nitro custard",
    "image": "https://i.imgur.com/Oe1SkiDm.png",
    "price": 59.50,
    "title": "lumapho berry nitro custard", 
    },

    {
    "category": "entree",
    "description": "dinoflagellate tonkotsu ramen",
    "image": "https://i.imgur.com/Qok48qOm.jpg",
    "price": 67.25,
    "title": "tonkotsu lumaramen", 
    },

    {
    "category": "entree",
    "description": "spinach pasta topped with mushrooms in a micro algae pesto",
    "image": "https://i.imgur.com/vJs4SfQm.jpg",
    "price": 67.00,
    "title": "microalgae pesto mushroom pasta", 
    },

    {
    "category": "entree",
    "description": "cryo-fried jellyfish replica, with a side of badlands-grown hydrugula. served with curried maize relish.",
    "id": 1,
    "image": "https://i.imgur.com/3uc6rnGm.jpg",
    "price": 58.5,
    "title": "midnight breakfast",
    },

    {
    "category": "entree",
    "description": "classic dish for sneaker heads. served with freshly printed pickles, onions, tomato, ketchup, mustard, mayo",
    "image": "https://i.imgur.com/uvYlmzrm.jpg",
    "price": 55.00,
    "title": "sneaker burger", 
    },

    {
    "category": "entree",
    "description": "live vivarium sliders, with bespoke mushroom patents",
    "image": "https://i.imgur.com/qqEfcFzm.jpg",
    "price": 0.0,
    "title": "vivarium sliders", 
    }
        ]

    dish_list = []

    for payload in payload_list:
        dish = models.Dish.create(**payload)
        dish_list.append(model_to_dict(dish))
    
    print(payload_list)

    return jsonify(
        data = dish_list,
        status = {
            "code": 201,
            "message": "🍛 Successfully seeded menu! 🥘"
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