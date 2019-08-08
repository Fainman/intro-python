"""
Use flight class
"""
from pprint import pprint as pp
from airtravel import Flight, Aircraft


def make_flight():
    a1 = Aircraft("G-EUP", "Airbus A319",
                  num_rows=22,
                  num_seats_per_row=6)

    f1 = Flight("SN063", a1)
    print(f1.number(), f1.airline())
    print(a1.registration(), a1.model())
    print(a1.seating_plan())
    f1.allocate_seat('12C', 'John')
    f1.allocate_seat('12D', 'James')
    return f1


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}" \
            "Flight: {1} " \
            "Seat: {2}"    \
            "Aircraft: {3}"\
            " |".format(passenger, flight_number, seat, aircraft)
    banner = "+" + "-" * (len(output)-2) + "+"
    border = "|" + " " * (len(output)-2) + "|"
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()


def main():
    """
    Test function
    :return: 
    """
    flight_1 = make_flight()
    pp(flight_1._seating)
    print("Available seats",
          flight_1.num_available_seats())
    flight_1.make_boarding_class(
        console_card_printer)
    print()


if __name__ == '__main__':
    main()
    exit(0)