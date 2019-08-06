"""
Learn about scoping in Python
"""
count = 0   # global object


def show_count():
    """
    Displays count
    :return: nothing
    """
    print(count)


def set_count(num):
    """
    Set Count
    :return: ntohing
    """
    global count
    count = num


def main():
    """
    Test function
    :return: 
    """
    show_count()
    set_count(9)
    show_count()
    print(count)


if __name__ == "__main__":
    main()
    exit(0)