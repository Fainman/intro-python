"""
Learn about exceptions
"""
import sys


def convert(s):
    """
    Converts a string to integer
    :param s: input string
    :return:
    """
    try:
        return int(s)
    except (TypeError, ValueError) as e:
        print("Conversion error {}"\
              .format(str(e)), file=sys.stderr)
        # print("Conversion failed!")
        # x = -1
    return -1


def sqrt(x):
    """

    :param x:
    :return:
    :raise ValueError() on ZeroDivisionError
    """
    guess = x
    i = 0
    try:
        while guess*guess != x and i < 20:
            guess = (guess + x/guess)/2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()
    return guess


def main():
    """
    Test function
    :return: 
    """
    # print(convert('11'))
    # print(convert('Hello'))
    # print(convert([1, 4, 8]))
    try:
        print(sqrt(9))
        print(sqrt(11))
        print(sqrt(-1))
    except ValueError:
        print("Cannot compute the value of negative numbers")
    print("Done")


if __name__ == "__main__":
    main()
    exit(0)