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
    "image": "nutrient_ dumplings.png",
    "price": 25.75,
    "title": "nutrient dumplings", 
    "labels": ["vegan", "fortified", "spicy", "ethically-sourced"]
    },

    {
    "category": "app",
    "description": "printed pizza bites with faux-mozzarella, basil, marinara concentrate, locally-grown micro-prosciutto",
    "image": "3D_printed_pizza_bites.jpeg",
    "price": 32.50,
    "title": "3D printed micro pizza", 
    "labels": ["lab-vegan", "ethically-sourced"]
    },

    {
    "category": "app",
    "description": "artisinally spliced fungi-pierogis with bespoke umami flavoring and exclusively patented mushroom blends",
    "image": "fungisphere.jpeg",
    "price": 47.00,
    "title": "fungisphere pierogis", 
    "labels": ["vegan", "ethically-sourced", "bespoke patent"]
    },

    {
    "category": "app",
    "description": "locally raised micro-koi atop a bed of protein-rice",
    "image": "microkoi_nigiri.jpeg",
    "price": 28.50,
    "title": "micro-koi nigiri", 
    "labels": ["pescatarian", "local"]
    },

    {
    "category": "app",
    "description": "10 multi-course meal bites, all individually blended classic flavor patents: chicken parmesan, mac-n-cheese casserole, cilantro-labneh, pork-jigae, black-truffled roast pork, octopus stifado, grilled hitaki, chipotle sesame shrimp, horse borsch, tabbouleh cremé",
    "image": "nitro_meal_spheres.jpeg",
    "price": 55.75,
    "title": "nitro meal spheres", 
    "labels": ["lab-vegan", "ethically-sourced", "spicy", "bespoke patent"]
    },

    {
    "category": "app",
    "description": "freshly pilled salad ingredients. mix and match!",
    "image": "pill_bites.jpeg",
    "price": 30.25,
    "title": "salad pill bites", 
    "labels": ["vegan", "ethically-sourced", "local"]
    },

    {
    "category": "app",
    "description": "perfectly balanced tomato basil soup dodecohedrons",
    "image": "tomato_basil_dodecohedrons.jpeg",
    "price": 42.0,
    "title": "tomato basil soup dodecohedrons", 
    "labels": ["vegan", "ethically-sourced", "bespoke patent"]
    },

    {
    "category": "app",
    "description": "neo-mediterranean salad sprout tarts",
    "image": "veggie_salad_tarts.jpeg",
    "price": 24.50,
    "title": "veggie salad tarts", 
    "labels": ["vegan", "ethically-sourced"]
    },

    # =============8 BEVS =================

    {
    "category": "bev",
    "description": "partially aerosolized cotton candy vodka tonic",
    "image": "cotton_vodka_tonic.jpeg",
    "price": 20.0,
    "title": "cotton candy vodka tonic", 
    "labels": ["alcoholic", "vodka", "sweet"]
    },

    {
    "category": "bev",
    "description": "old-world cuban rum and reconstituted micro-fruit blend with simply syrup",
    "image": "fruitini.jpeg",
    "price": 24.00,
    "title": "fruitini", 
    "labels": ["alcoholic", "rum", "sweet", "fruity"]
    },

    {
    "category": "bev",
    "description": "wide variety of beer flavored malt liquors",
    "image": "happochu.jpeg",
    "price": 14.50,
    "title": "happochu", 
    "labels": ["alcoholic", "malt liquor"]
    },

    {
    "category": "bev",
    "description": "luma take on an old classic gin and tonic",
    "image": "luma_GnT.jpeg",
    "price": 20.00,
    "title": "luma GnT", 
    "labels": ["alcoholic", "gin", "classic", "glowing"]
    },

    {
    "category": "bev",
    "description": "a neosaka classic: espresso, matcha and chipotle oil",
    "image": "neospresso.jpeg",
    "price": 12.75,
    "title": "neospresso", 
    "labels": ["caffeine", "matcha", "spicy"]
    },

    {
    "category": "bev",
    "description": "gelatinized portable coffee",
    "image": "portable_coffee_cubes.jpeg",
    "price": 11.50,
    "title": "portable coffee cubes", 
    "labels": ["caffeine", "candy"]
    },

    {
    "category": "bev",
    "description": "rum, tequila, dinoflagellate-infused mescalina, simple syrup, aromatics",
    "image": "the_vortex.jpeg",
    "price": 52.75,
    "title": "the vortex", 
    "labels": ["alcoholic", "psychoactive", "glowing"]
    },

    {
    "category": "bev",
    "description": "500ml gelatinized water modules",
    "image": "water.jpeg",
    "price": 19.50,
    "title": "water", 
    "labels": ["hydrating"]
    },

    # =============7 DESSERTS=================

    {
    "category": "dessert",
    "description": "printed candied marzipan skulls. flavors include: chocolate walnut, bubblegum, fresh fruit",
    "image": "3D_printed_candied_marzipan_skulls.jpeg",
    "price": 28.50,
    "title": "3D printed candied marzipan skulls", 
    "labels": ["candy", "sweet", "vegetarian"]
    },

    {
    "category": "dessert",
    "description": "3D printed mini chocolate apple pies",
    "image": "3d_printed_mini_apple_pies.jpeg",
    "price": 35.00,
    "title": "mini chocolate apple pies", 
    "labels":  ["chocolate", "sweet", "vegetarian"]
    },

    {
    "category": "dessert",
    "description": "layered dinoflagellate-infused glazed focaccia",
    "image": "luma_bread.jpeg",
    "price": 20.0,
    "title": "luma bread", 
    "labels":  [ "sweet", "vegetarian", "glowing"]
    },

    {
    "category": "dessert",
    "description": "glazed donuts with dinoflagellate-infused icing. three to an order",
    "image": "luma_donuts.jpeg",
    "price": 26.50,
    "title": "luma donuts", 
    "labels": [ "sweet", "vegetarian", "glowing"]
    },

    {
    "category": "dessert",
    "description": "stack of 5 micro algae pancakes topped with syrup, whipped cream and freshly printed fruit",
    "image": "microalgae_pancakes.jpeg",
    "price": 32.0,
    "title": "microalgae pancakes", 
    "labels": [ "sweet", "vegetarian"]
    },

    {
    "category": "dessert",
    "description": "combined dna from fish roe for structure and raspberries for flavor, we’ve created this unique dessert experience",
    "image": "reconstructed_berry_roe.jpeg",
    "price": 49.50,
    "title": "reconstructed berry roe", 
    "labels": ["label1", "label2", "label3"]
    },

    {
    "category": "dessert",
    "description": "another unique experience: live pomegranate injected white chocolate torte",
    "image": "reconstructed_white_pomegranate.jpeg",
    "price": 0.0,
    "title": "reconstructed white pomegranate torte", 
    "labels": ["label1", "label2", "label3"]
    },

    # =============16 ENTREES=================

    {
    "category": "entree",
    "description": "citrus braised cicada salad with badlands sea-salt and post-peruvian pepper",
    "image": "braised_cicada_salad.jpeg",
    "price": 63.00,
    "title": "braised cicada salad", 
    "labels": ["insect", "savory"]
    },

    {
    "category": "entree",
    "description": "cajun-boiled recombined crawlobster with braised spinach",
    "image": "crawlobster_spinach_bowl.jpeg",
    "price": 67.50,
    "title": "crawlobster spinach bowl", 
    "labels": ["recombined", "seafood", "pescatarian", "spicy"]
    },

    {
    "category": "entree",
    "description": "a neosaka classic: cricket okonomiyaki",
    "image": "cricket_okonomiyaki.jpeg",
    "price": 59.75,
    "title": "cricket okonomiyaki", 
    "labels": ["insect", "savory"]
    },

    {
    "category": "entree",
    "description": "wild trychopeplus fortified with vitamin bundle and neurotropic enhancements. serves 2",
    "image": "fortified_ wild_trychopeplus.jpeg",
    "price": 275.50,
    "title": "fortified wild trychopeplus", 
    "labels": ["insect", "savory", "neurotropic enhancement", "fortified"]
    },

    {
    "category": "entree",
    "description": "reconstituted turkey dinner, perfectly indocharged to temperature. *please specify if desired temp is other than medium.",
    "image":  "indocharged_turkey_dinner.jpeg",
    "price": 73.00,
    "title": "indocharged turkey dinner", 
    "labels": ["indocharged", "poultry", "savory"]
    },

    {
    "category": "entree",
    "description": "roasted squid filled dinoflagellate-infused crepes with algae sauce",
    "image": "lumabite_squid_crepes.jpeg",
    "price": 68.75,
    "title": "lumabite squid crepes", 
    "labels": [ "seafood", "pescatarian", "savory"]
    },

    {
    "category": "entree",
    "description": "dinoflagellate-infused sushi box: maguro, salmon, ebi",
    "image": "lumabite_sushi_box.jpeg",
    "price": 75.00,
    "title": "lumabite sushi box", 
    "labels": ["sushi", "glowing"]
    },

    {
    "category": "entree",
    "description": "tamago pho with bok chow, carrot and mushroom rings. served with s side of berry nitro custard",
    "image": "lumapho_berry_nitro_custard.jpeg",
    "price": 59.50,
    "title": "lumapho berry nitro custard", 
    "labels": ["glowing", "combo", "vegetarian", "soup", "savory"]
    },

    {
    "category": "entree",
    "description": "deconstructed dinoflagellate tamago ramen",
    "image": "lumaramen_bowl.jpeg",
    "price": 62.50,
    "title": "lumaramen bowl", 
    "labels": ["glowing", "soup", "savory"]
    },

    {
    "category": "entree",
    "description": "dinoflagellate tonkotsu ramen",
    "image": "lumaramen_bowl2.jpeg",
    "price": 67.25,
    "title": "tonkotsu lumaramen", 
    "labels": ["glowing", "soup", "savory"]
    },

    {
    "category": "entree",
    "description": "spinach pasta topped with mushrooms in a micro algae pesto",
    "image": "microalgae_pesto_mushroom_pasta.jpeg",
    "price": 67.00,
    "title": "microalgae pesto mushroom pasta", 
    "labels": ["pasta", "vegan", "savory"]
    },

    {
    "category": "entree",
    "description": "cryo-fried jellyfish replica, with a side of badlands-grown hydrugula. served with curried maize relish.",
    "id": 1,
    "image": "midnight_breakfast.jpeg",
    "price": 58.5,
    "title": "midnight breakfast",
    "labels": ["pescatarian", "spicy"]
    },

    {
    "category": "entree",
    "description": "classic dish for sneaker heads. served with freshly printed pickles, onions, tomato, ketchup, mustard, mayo",
    "image": "sneaker_burger.jpeg",
    "price": 55.00,
    "title": "sneaker burger", 
    "labels": ["reconstituted beef"]
    },

    {
    "category": "entree",
    "description": "live vivarium sliders, with bespoke mushroom patents",
    "image": "vivarium_sliders.jpeg",
    "price": 0.0,
    "title": "vivarium sliders", 
    "labels": ["vegan", "ethically-sourced", "bespoke patent"]
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