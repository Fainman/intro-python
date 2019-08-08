"""
Use flight class
"""
from pprint import pprint as pp
from airtravel import Flight, Aircraft


def main():
    """
    Test function
    :return: 
    """

    a1 = Aircraft("G-EUP", "Airbus A319",
                  num_rows=22,
                  num_seats_per_row=6)

    f1 = Flight("SN063", a1)
    print(f1.number(), f1.airline())
    print(a1.registration(), a1.model())
    print(a1.seating_plan())
    pp(f1._seating)
    f1.allocate_seat('12C', 'John')
    f1.allocate_seat('12D', 'James')
    pp(f1._seating)


if __name__ == '__main__':
    main()
    exit(0)