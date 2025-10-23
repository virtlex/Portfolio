"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]
    
#print(get_coordinate(('Scrimshawed Whale Tooth', '2A')))

def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    cordy = tuple (coordinate)
    return cordy
#print(convert_coordinate("2A"))


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    kordy1 = convert_coordinate(azara_record[1])
    if kordy1 == rui_record[1]:
        return True
    else:
        return False

#print(compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple')))


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    kordy1 = convert_coordinate(azara_record[1])
    if kordy1 == rui_record[1]:
        return azara_record + rui_record
    else:
        return "not a match"

#print(create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue')))

def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    report = ""
    for record in combined_record_group:
        report += str(record[:1] + record[2:]) + "\n"
    return report

#print(clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))))