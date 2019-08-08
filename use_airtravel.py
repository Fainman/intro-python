"""
Use flight class
"""

from airtravel import Flight, Aircraft


def main():
    """
    Test function
    :return: 
    """
    f = Flight("SN066")
    print(f, type(f))
    print(f.number(), f.airline())
    # Because we use self, don't need Flight.number(f)

    f2 = Flight("SN063")
    print(f2.number(), f2.airline())

    a1 = Aircraft("G-EUP", "Airbus A319",
                  num_rows=22,
                  num_seats_per_row=6)
    print(a1.registration(), a1.model())


if __name__ == '__main__':
    main()
    exit(0)