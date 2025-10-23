"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats = ["A","B","C","D"]
    for i in range(number):
        yield seats[i % 4]
    

#letters = generate_seat_letters(50)


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    row = 0
    seats = ["A","B","C","D"]
    for i in range(number):
        if i % 4 == 0:
            row +=1
        if row == 13:
            row +=1    
        yield str(row) + seats[i % 4]

#seats = generate_seats(150)


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    board = {}
    seat_gen=generate_seats(len(passengers))
    for passenger in passengers:
        board[passenger] = next(seat_gen)
    print(board)
    return board

#passengers = ['Jerimiah', 'Eric', 'Bethany', 'Byte', 'SqueekyBoots', 'Bob']
#assign_seats(passengers)


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        ticket= seat+flight_id
        chars= len(ticket)
        if chars != 12:
            zera = 12- chars
            ticket += 12-chars*"0"
        yield ticket


#flight_id = 'CO12'
#seat_numbers = ['1A', '17D']
#ticket_ids = generate_codes(seat_numbers, flight_id)
#print(next(ticket_ids))
#print(next(ticket_ids))



