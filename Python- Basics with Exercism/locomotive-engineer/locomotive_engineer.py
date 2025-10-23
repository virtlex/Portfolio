"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*arg):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    train = []
    for cargo in arg:
        train.append(cargo)
    #print(train)
    return train


#get_list_of_wagons(1, 7, 12, 3, 14, 8, 5)



def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    i=2
    train = []
    [a, b ,c, *arg] = each_wagons_id  
    train.append(c)
    for id in missing_wagons:
        train.insert(i,id)
        i+=1
    for id in arg:
        train.append(id)
    train.append(a)
    train.append(b)
    print(train)
    return train
fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])
    

def add_missing_stops(directory, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    lista = []
    for key, value in kwargs.items():
        #lista.append(key)
        lista.append(value)
    directory["stops"] = lista
    #print(directory)
    return directory
'''
add_missing_stops({"from": "New York", "to": "Miami"},
                      stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
                     stop_4="Jacksonville", stop_5="Orlando")
'''

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    info = route | more_route_information
    #print(info)
    return info
#extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"})


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    depot = []
    litA = []
    litB = []
    litC = []
    i=0
    for color in wagons_rows:
        a,b,c = color
        litA.append(a)
        litB.append(b)
        litC.append(c)

    depot.append(litA)
    depot.append(litB)
    depot.append(litC)
    #print(depot)
    return depot

#fix_wagon_depot([
#                    [(2, "red"), (4, "red"), (8, "red")],
#                    [(5, "blue"), (9, "blue"), (13,"blue")],
#                    [(3, "orange"), (7, "orange"), (11, "orange")],
#                    ])