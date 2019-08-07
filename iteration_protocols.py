"""
Learn about iterable, iterator objects
Use the built-in in:
 iter(): create an iterable object,
 next(): fetch the next element in the iterable object
"""


def main():
    """
    Test function
    :return: 
    """
    iterable = ["Spring", "Summer", "Fall", "Winter"]
    iterator = iter(iterable)  # give me an iterator
    print(type(iterator), iterator)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    output = first(iterable)
    print(output)


def first(iterable):
    """
    Return the next member of the list if available
    :param iterable: iterable object
    :return: Next member or
    :except: ValueError for StopIteration
    """
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")


if __name__ == "__main__":
    main()
    exit(0)