"""
Description
"""


def main():
    """
    Test function
    :return:
    """
    # Default
    for i in range(5):
        print(i)

    # Set the initial value:
    for i in range(5, 10):
        print(i)

    # Create a list from range
    l = list(range(5, 10))
    print(l)
    l2 = list(range(5, 10)) + list(range(30, 40))
    print(l2, type(l2))
    # Step argument: (begin, end, step)
    l3 = list(range(0, 20, 2))
    print(l3)
    # Iteration over list using index notation
    s = [0, 2, 3, 4, 6]
    for i in range(len(s)):
        print(s[i])
    # Better way
    for v in s:
        print(v)

    # enumerate(): returns an iterable series
    t = [6, 789, 123, 98, 3, 22]
    for p, q in enumerate(t):
        print(p, q)
        print("i = {}, v = {}".format(p, q))




if __name__ == "__main__":
    main()
    exit(0)