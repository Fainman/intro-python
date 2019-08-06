"""
Learn about Python return semantics and how Python functions handle arguments
"""

def egg(var):
    """
    returns the variable back to the user
    :param var: input object
    :return: input object
    """
    return var


def sum_two(num1, num2=8):
    """
    Sum two numbers
    :param num1: input first variable
    :param num2: input second variable
    :return: sum of objects
    """
    return num1 + num2


def banner(message, border='*'):
    print(border * (4 + len(message)))
    print(border, message, border)
    print(border * (4 + len(message)))


def add_spam(menu=None):
    """
    Add spam to the menu list
    :param menu: input menu list
    :return: menu list
    """
    if menu is None:
        menu = []

    menu.append('spam')
    return menu


def main():
    """
    Test function
    :return:
    """
    banner('my message', '-')
    c = [6, 10, 20]
    e = egg(c)
    print(c is e)
    print(sum_two([2], [5]))
    print(sum_two(2))
    my_menu = ['eggs', 'sausage']
    add_spam(my_menu)
    print(my_menu)


if __name__ == "__main__":
    main()
    exit(0)