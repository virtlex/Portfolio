"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    backpack = {}
    for item in items:
        if item in backpack:
            backpack[item] += 1
        else:
            backpack[item] = 1
    return backpack

#print(create_inventory(["wood", "iron", "iron", "diamond", "diamond"]))


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

#add_items({"coal":1}, ["wood", "iron", "coal", "wood"])



def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if item in inventory:
            if inventory[item] == 0:
                continue
            else:
                inventory[item] -= 1
    return inventory

#decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"])

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    d = inventory.copy()
    for items in d:
        if item == items:
            inventory.pop(item)
        else:

            continue
    return inventory

#print(remove_item({"iron": 1, "diamond": 2, "gold": 1}, "diamond"))


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inv_list = []
    for item in inventory:
        if inventory[item] > 0:
            inv_list.append((item,inventory[item]))
        else:
            continue
    return inv_list

print(list_inventory({"coal": 15, "diamond": 3, "wood": 67, "silver": 0}))
