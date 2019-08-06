"""
File learn about collection: Tuples, Strings, Range, List, Dictionaries, and Sets
"""

def do_tuples():
    """
    Practice tuples
    :return: nothing
    """
    # Immutable sequence of arbitrary objects
    # Use () to define a tuple
    t = ("Ogden", 1.99, 2)
    print(t, type(t))
    print("Size ", len(t))
    print("One member", t[0])
    for item in t:
        print(item)

    # Single tuples, must end with comma
    t1 = (6,)
    print(t1, type(t1))

    # Another way to create tuples
    # Parenthesis are optional
    t2 = 1, 2, 3, 5
    print(t2, type(t2))

    # Tuple constructor: tuple()
    t_from_l = tuple([3, 77, 11])
    print(t_from_l, type(t_from_l))

    # test for membership
    print(5 in (3, 6, 8, 5, 12))
    print(5 not in (3, 6, 8, 5, 12))


def min_max(items):
    """
    Return the minimum and maximum
    :param items: collection
    :return: the minimum and maximum
    """
    return min(items), max(items)


def swap(var1, var2):
    """
    Swap the values of two variables
    :param var1: first variable
    :param var2: second variable
    :return: both variables, swapped
    """
    return var2, var1


def main():
    """
    Test function
    :return: 
    """
    do_tuples()
    output = min_max([1, 2, 3, 4, 5, 6])
    print("min", output[0])
    print("max", output[1])
    # Tuple unpacking
    lower, upper = min_max([1, 2, 3, 4, 5, 6])
    print("min", lower)
    print("max", upper)
    a = 3
    b = 4
    print(a, b)
    a, b = swap(a, b)
    print(a, b)


if __name__ == "__main__":
    main()
    exit(0)