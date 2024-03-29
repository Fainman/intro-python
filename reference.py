"""

Learn about references
"""


def modify(k):
    """
    Modify the content of a list
    :param k: a list
    :return: nothing
    """
    print(id(k))
    # list are passed by reference
    k.append(39)
    print("k = ", k)


def replace(g):
    """
    Replace input list
    :param g: input list
    :return: nothing
    """
    g = [17, 48, 89]
    print("g = ", g)


def replace_content(g):
    """
    Replace the content of the input list
    :param g: input list
    :return: nothing
    """
    g[0] = 88
    g[1] = 22
    g[2] = 44
    print("g = ", g)

def main():
    """
    test function
    :return: nothing
    """
    m = [9, 15, 24]
    print(id(m))
    print("Before m = ", m)
    modify(m)
    print("After m = ", m)
    replace(m)
    print("After replace() m = ", m)
    replace_content(m)
    print("After replace content() m = ", m)


if __name__ == "__main__":
    main()
    exit(0)