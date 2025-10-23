"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    round= [number, number+1, number+2]
    print (round)
    return round


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    round = rounds_1 + rounds_2
    print(round)
    return round



def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in rounds:
        return True
    else:
        return False



def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    score = sum(hand)/len(hand)

    return score



def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    act = card_average(hand)
    score = (hand[0] + hand[-1])/2
    mediana= len(hand)//2
    if act == score or act == hand[mediana]:
        return True
    else:
        return False
#print(approx_average_is_average([2, 3, 4, 8, 8]))

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    return card_average(hand[0::2]) == card_average(hand[1::2])
print(average_even_is_average_odd([1, 3, 5, 7, 9]))

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = hand[-1]*2 
        print (hand)
        return hand
    else:
        new_hand= hand
        print (new_hand)
        return hand

hand = [5, 9, 11]
#maybe_double_last(hand)

