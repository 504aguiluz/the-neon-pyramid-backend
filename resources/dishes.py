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
    "qtyOrdered": 0,
    "category": "app",
    "description": "six nutrient-fortified dumplings: flavors based on the cuisine of each sector in Neo-saka.",
    "image": "https://i.imgur.com/wLIpX96t.png",
    "price": 25.75,
    "title": "nutrient dumplings", 
    # "labels": ["vegan", "fortified", "spicy", "ethically-sourced"]
    },

    {
    "qtyOrdered": 0,
    "category": "app",
    "description": "printed pizza bites with faux-mozzarella, basil, marinara concentrate, locally-grown micro-prosciutto",
    "image": "https://i.imgur.com/06TfTimt.jpg",
    "price": 32.50,
    "title": "3D printed micro pizza", 
    # "labels": ["lab-vegan", "ethically-sourced"]
    },

    {
    "qtyOrdered": 0,  
    "category": "app",
    "description": "artisinally spliced fungi-pierogis with bespoke umami flavoring and exclusively patented mushroom blends",
    "image": "https://i.imgur.com/H49qi2Vt.jpg",
    "price": 47.00,
    "title": "fungisphere pierogis", 
    # "labels": ["vegan", "ethically-sourced", "bespoke patent"]
    },

    {
    "qtyOrdered": 0,
    "category": "app",
    "description": "locally raised micro-koi atop a bed of protein-rice",
    "image": "https://i.imgur.com/u7gDLK1t.jpg",
    "price": 28.50,
    "title": "micro-koi nigiri", 
    "labels": ["pescatarian", "local"]
    },

    {
    "qtyOrdered": 0,
    "category": "app",
    "description": "10 multi-course meal bites, all individually blended classic flavor patents: chicken parmesan, mac-n-cheese casserole, cilantro-labneh, pork-jigae, black-truffled roast pork, octopus stifado, grilled hitaki, chipotle sesame shrimp, horse borsch, tabbouleh cremé",
    "image": "https://i.imgur.com/W6n28qzt.jpg",
    "price": 55.75,
    "title": "nitro meal spheres", 
    # "labels": ["lab-vegan", "ethically-sourced", "spicy", "bespoke patent"]
    },

    {
    "qtyOrdered": 0,
    "category": "app",
    "description": "freshly pilled salad ingredients. mix and match!",
    "image": "https://i.imgur.com/u8Vtyayt.jpg",
    "price": 30.25,
    "title": "salad pill bites", 
    # "labels": ["vegan", "ethically-sourced", "local"]
    },

    {
    "qtyOrdered": 0,
    "category": "app",
    "description": "perfectly balanced tomato basil soup dodecohedrons",
    "image": "https://i.imgur.com/7wGpLnwt.jpg?2",
    "price": 42.0,
    "title": "tomato basil soup dodecohedrons", 
    # "labels": ["vegan", "ethically-sourced", "bespoke patent"]
    },

    {
    "qtyOrdered": 0,
    "category": "app",
    "description": "neo-mediterranean salad sprout tarts",
    "image": "https://i.imgur.com/xKOpIuKt.jpg",
    "price": 24.50,
    "title": "veggie salad tarts", 
    # "labels": ["vegan", "ethically-sourced"]
    },

    # =============8 BEVS =================

    {
    "qtyOrdered": 0,
    "category": "bev",
    "description": "partially aerosolized cotton candy vodka tonic",
    "image": "https://i.imgur.com/tmE0C7Mt.png",
    "price": 20.0,
    "title": "cotton candy vodka tonic", 
    # "labels": ["alcoholic", "vodka", "sweet"]
    },

    {
    "qtyOrdered": 0,
    "category": "bev",
    "description": "old-world cuban rum and reconstituted micro-fruit blend with simply syrup",
    "image": "https://i.imgur.com/c2xc7XBt.jpg",
    "price": 24.00,
    "title": "fruitini", 
    # "labels": ["alcoholic", "rum", "sweet", "fruity"]
    },

    {
    "qtyOrdered": 0,
    "category": "bev",
    "description": "wide variety of beer flavored malt liquors",
    "image": "https://i.imgur.com/UDtgOl1t.jpg",
    "price": 14.50,
    "title": "happochu", 
    # "labels": ["alcoholic", "malt liquor"]
    },

    {
    "qtyOrdered": 0,
    "category": "bev",
    "description": "luma take on an old classic gin and tonic",
    "image": "https://i.imgur.com/HwTB6but.jpg",
    "price": 20.00,
    "title": "luma GnT", 
    # "labels": ["alcoholic", "gin", "classic", "glowing"]
    },

    {
    "qtyOrdered": 0,
    "category": "bev",
    "description": "a neosaka classic: espresso, matcha and chipotle oil",
    "image": "https://i.imgur.com/ngzpE6Ft.jpg",
    "price": 12.75,
    "title": "neospresso", 
    # "labels": ["caffeine", "matcha", "spicy"]
    },

    {
    "qtyOrdered": 0,
    "category": "bev",
    "description": "gelatinized portable coffee",
    "image": "https://i.imgur.com/qEPbJsut.png",
    "price": 11.50,
    "title": "portable coffee cubes", 
    # "labels": ["caffeine", "candy"]
    },

    {
    "qtyOrdered": 0,
    "category": "bev",
    "description": "rum, tequila, dinoflagellate-infused mescalina, simple syrup, aromatics",
    "image": "https://i.imgur.com/8YrFz9Ht.jpg",
    "price": 52.75,
    "title": "the vortex", 
    # "labels": ["alcoholic", "psychoactive", "glowing"]
    },

    {
    "qtyOrdered": 0,
    "category": "bev",
    "description": "500ml gelatinized water modules",
    "image": "https://i.imgur.com/k7el2fPt.jpg",
    "price": 19.50,
    "title": "water", 
    # "labels": ["hydrating"]
    },

    # =============7 DESSERTS=================

    {
    "qtyOrdered": 0,
    "category": "dessert",
    "description": "printed candied marzipan skulls. flavors include: chocolate walnut, bubblegum, fresh fruit",
    "image": "https://i.imgur.com/iTnXAgrt.jpg",
    "price": 28.50,
    "title": "3D printed candied marzipan skulls", 
    # "labels": ["candy", "sweet", "vegetarian"]
    },

    {
    "qtyOrdered": 0,
    "category": "dessert",
    "description": "3D printed mini chocolate apple pies",
    "image": "https://i.imgur.com/cyju2GPt.png",
    "price": 35.00,
    "title": "mini chocolate apple pies", 
    # "labels":  ["chocolate", "sweet", "vegetarian"]
    },

    {
    "qtyOrdered": 0,
    "category": "dessert",
    "description": "layered dinoflagellate-infused glazed focaccia",
    "image": "https://i.imgur.com/JCrUXO6t.png",
    "price": 20.0,
    "title": "luma bread", 
    # "labels":  [ "sweet", "vegetarian", "glowing"]
    },

    {
    "qtyOrdered": 0,
    "category": "dessert",
    "description": "glazed donuts with dinoflagellate-infused icing. three to an order",
    "image": "https://i.imgur.com/XaCFREmt.jpg",
    "price": 26.50,
    "title": "luma donuts", 
    # "labels": [ "sweet", "vegetarian", "glowing"]
    },

    {
    "qtyOrdered": 0,
    "category": "dessert",
    "description": "stack of 5 micro algae pancakes topped with syrup, whipped cream and freshly printed fruit",
    "image": "https://i.imgur.com/d6OdU5zt.jpg",
    "price": 32.0,
    "title": "microalgae pancakes", 
    # "labels": [ "sweet", "vegetarian"]
    },

    {
    "qtyOrdered": 0,
    "category": "dessert",
    "description": "combined dna from fish roe for structure and raspberries for flavor, we’ve created this unique dessert experience",
    "image": "https://i.imgur.com/VnONfF2t.jpg",
    "price": 49.50,
    "title": "reconstructed berry roe", 
    # "labels": ["label1", "label2", "label3"]
    },

    {
    "qtyOrdered": 0,
    "category": "dessert",
    "description": "another unique experience: live pomegranate injected white chocolate torte",
    "image": "https://i.imgur.com/ez2XJ57t.jpg",
    "price": 0.0,
    "title": "reconstructed white pomegranate torte", 
    # "labels": ["label1", "label2", "label3"]
    },

    # =============16 ENTREES=================

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "citrus braised cicada salad with badlands sea-salt and post-peruvian pepper",
    "image": "https://i.imgur.com/ENkSPndt.jpg",
    "price": 63.00,
    "title": "braised cicada salad", 
    # "labels": ["insect", "savory"]
    },

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "cajun-boiled recombined crawlobster with braised spinach",
    "image": "https://i.imgur.com/Rq1jG0Ut.jpg",
    "price": 67.50,
    "title": "crawlobster spinach bowl", 
    # "labels": ["recombined", "seafood", "pescatarian", "spicy"]
    },

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "a neosaka classic: cricket okonomiyaki",
    "image": "https://i.imgur.com/wu0JRoMt.jpg",
    "price": 59.75,
    "title": "cricket okonomiyaki", 
    # "labels": ["insect", "savory"]
    },

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "wild trychopeplus fortified with vitamin bundle and neurotropic enhancements. serves 2",
    "image": "https://i.imgur.com/J4WGuC0t.jpg",
    "price": 275.50,
    "title": "fortified wild trychopeplus", 
    # "labels": ["insect", "savory", "neurotropic enhancement", "fortified"]
    },

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "reconstituted turkey dinner, perfectly indocharged to temperature. *please specify if desired temp is other than medium.",
    "image":  "https://i.imgur.com/zjsFRM2t.jpg",
    "price": 73.00,
    "title": "indocharged turkey dinner", 
    # "labels": ["indocharged", "poultry", "savory"]
    },

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "roasted squid filled dinoflagellate-infused crepes with algae sauce",
    "image": "https://i.imgur.com/XwM3ttht.jpg",
    "price": 68.75,
    "title": "lumabite squid crepes", 
    # "labels": [ "seafood", "pescatarian", "savory"]
    },

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "dinoflagellate-infused sushi box: maguro, salmon, ebi",
    "image": "https://i.imgur.com/bPHIOSOt.jpg",
    "price": 75.00,
    "title": "lumabite sushi box", 
    # "labels": ["sushi", "glowing"]
    },

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "tamago pho with bok chow, carrot and mushroom rings. served with a side of berry nitro custard",
    "image": "https://i.imgur.com/Oe1SkiDt.png",
    "price": 59.50,
    "title": "lumapho berry nitro custard", 
    # "labels": ["glowing", "combo", "vegetarian", "soup", "savory"]
    },

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "deconstructed dinoflagellate tamago ramen",
    "image": "https://i.imgur.com/Oe1SkiDt.png",
    "price": 62.50,
    "title": "lumaramen bowl", 
    # "labels": ["glowing", "soup", "savory"]
    },

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "dinoflagellate tonkotsu ramen",
    "image": "https://i.imgur.com/Qok48qOt.jpg",
    "price": 67.25,
    "title": "tonkotsu lumaramen", 
    # "labels": ["glowing", "soup", "savory"]
    },

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "spinach pasta topped with mushrooms in a micro algae pesto",
    "image": "https://i.imgur.com/vJs4SfQt.jpg",
    "price": 67.00,
    "title": "microalgae pesto mushroom pasta", 
    # "labels": ["pasta", "vegan", "savory"]
    },

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "cryo-fried jellyfish replica, with a side of badlands-grown hydrugula. served with curried maize relish.",
    "id": 1,
    "image": "https://i.imgur.com/3uc6rnGt.jpg",
    "price": 58.5,
    "title": "midnight breakfast",
    # "labels": ["pescatarian", "spicy"]
    },

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "classic dish for sneaker heads. served with freshly printed pickles, onions, tomato, ketchup, mustard, mayo",
    "image": "https://i.imgur.com/uvYlmzrt.jpg",
    "price": 55.00,
    "title": "sneaker burger", 
    # "labels": ["reconstituted beef"]
    },

    {
    "qtyOrdered": 0,
    "category": "entree",
    "description": "live vivarium sliders, with bespoke mushroom patents",
    "image": "https://i.imgur.com/qqEfcFzt.jpg",
    "price": 0.0,
    "title": "vivarium sliders", 
    # "labels": ["vegan", "ethically-sourced", "bespoke patent"]
    }
        ]

    dish_list = []

    for payload in payload_list:
        dish = models.Dish.create(**payload)
        dish_list.append(dish)


    seeded_dishes = model_to_dict(dish_list)
    return jsonify(
        data = seeded_dishes,
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