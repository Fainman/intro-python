"""
A Flight Class. Model for aircraft flights
"""


class Flight:
    """
    A Flight wit ha particular passenger aircraft
    """
    def __init__(self, number):
        # Validate flight number:
        # 5 chars long: AADDD A-> Alpha, D->Digit
        if len(number) != 5:
            raise ValueError("Invalid flight number length".format(number))
        if not number[:2].isalpha():
            raise ValueError("Invalid flight number. First two must be alpha".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid flight number. First two must be uppercase".format(number))
        if not number[3:].isdecimal():
            raise ValueError("Invalid flight number. Last three must be numeric".format(number))
        self._number = number  # implementation details begin with '_'

    def number(self):
        """
        Flight Number
        :return: flight number
        """
        return self._number[2:]

    def airline(self):
        """
        Return airline code
        :return: Two letter, uppercase airline code
        """
        return self._number[:2]


class Aircraft:
        def __init__(self, registration, model, num_rows,
                     num_seats_per_row):
            self._registration = registration
            self._model = model
            self._num_rows = num_rows
            self._num_seats_per_row = num_seats_per_row

        def registration(self):
            return self._registration

        def model(self):
            return self._model


def main():
    """
    Test function
    :return: 
    """
    pass


if __name__ == '__main__':
    main()
    exit(0)