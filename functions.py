"""

Learn about definitions (aka functions)
Use the keyword: def <name>():
"""


def even_or_odd(number):
    """
    Find if number is even or odd.
    "even" on even numbers
    "odd" on odd numbers
    :param number: input number
    :return: N/A
    """
    if number % 2 == 0:
        print('even')
    else:
        print('odd')

def main():
    """
    Test Function
    :return:
    """
    # Call function
    print(__name__)
    even_or_odd(89)
    even_or_odd(22)

if __name__ == "__main__":
    main()
    exit(0)