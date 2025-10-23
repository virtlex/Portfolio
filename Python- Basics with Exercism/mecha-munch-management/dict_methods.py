"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    #print(current_cart)
    return current_cart

#add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},('Apple', 'Apple', 'Orange', 'Apple', 'Banana'))


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart ={}
    for item in notes:
        cart.setdefault(item, 1)
    #print (cart)
    return cart
# read_notes(('Banana','Apple', 'Orange'))

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas

#update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},(('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),))

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    sorted_cart = sorted(cart.items())
    #print (sorted_cart)
    return sorted_cart

#sort_entries({'Banana': 3, 'Apple': 2, 'Orange': 1})

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_dict={}
    for item in cart.keys():
        aisle_mapping[item].insert(0,cart[item])
        fulfillment_dict[item]=aisle_mapping[item]
    new_dict={}
    new_dict |= reversed(sorted(fulfillment_dict.items()))
    #print(new_dict)
    return new_dict
#send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},{'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]})

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for key in fulfillment_cart.keys():
        store_inventory[key][0] -= fulfillment_cart[key][0]
        #print(store_inventory)
        if store_inventory[key][0] <= 0:
            store_inventory[key][0] = "Out of Stock"
    #print (store_inventory)
    return store_inventory 
            
#update_store_inventory({'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},{'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]})

