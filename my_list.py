"""
Learn about list()
"""


def main():
    """
    Test function
    :return: 
    """
    s = "show how to do it".split()
    print(s, type(s))
    # Access by index
    print("s[3]", s[3])
    print("last member", s[len(s)-1]) # very unpythonic
    # Use negative index
    print("s[-1]:", s[-1])
    # Slicing
    print("From 1 to one before the last", s[1:-1])
    print("From 1 to the end", s[1:])
    print("From beginning to 3", s[:3])
    print("From beg to end", s[:])
    # Make a copy of list
    t = s # Shallow copy - only copies the reference
    print("t is s", t is s)
    t = s[:] # Deep copy - creates new t and assigns values
    # or this: t = s.copy()
    # or this: t = list(s)
    print("t is s", t is s)
    print("t == s", t == s)
    print("t is s", t[0] is s[0])

    # Shallow copies
    # A list of list
    a = [[1, 2], [3, 4]]
    print(a, type(a))
    print("a[0]:", a[0])
    print("a[0][1]:", a[0][1])

    # Deep copies
    b = a[:]
    print("a is b", a is b)
    print("a == b", a == b)
    print("a[0]", a[0])
    print("b[0]", b[0])
    print("a[0] is b[0]", a[0] is b[0])
    a[0] = [8, 9]
    print("a[0]", a[0])
    print("b[0]", b[0])
    print("a[0] is b[0]", a[0] is b[0])
    # Repetition
    c = [21, 37]
    d = c * 4
    print("c", c)
    print("d", d)
    s = [[-1, 1]] * 5
    print(s)
    # index()
    w = "the quick brown fox jumps over the lazy dog".split()
    i = w.index('fox')
    print("The index of 'fox' entry is:", i)
    # IF no index is found, it will throw a ValueError
    # i = w.index('cat')
    # print("The index of 'fox' entry is:", i)

    # Membership testing with: count()
    print("'the' occurs this many times:", w.count('the'))
    # Also test membership with: in, not in
    print(37 in [12, 22, 37, 99])
    print(78 not in [12, 22, 37, 99])
    # Removing elements form list: index and del
    w = "the quick brown fox jumps over the lazy dog".split()
    print(w)
    del w[3]
    print(len(w), w)
    # Remove using: remove()
    w.remove("over")
    print(len(w), w)
    # same as
    del w[w.index('dog')]
    print(len(w), w)
    # Rearranging list of elements
    g = [1, 11, 21, 1211, 112111]
    print("g:", g)
    g.reverse()
    print("reverse g:", g)

    # Sort method accepts two arguments
    d = [21, 33, 11, 77, 88, 33, 101, 1]
    print(d)
    d.sort()
    print(d)
    d.sort(reverse=True)
    print("sort.reverse d:", d)
    # Sort by key
    w = "the quick brown fox jumps over the lazy dog".split()
    print(w)
    w.sort(key = len)
    print(w)


if __name__ == "__main__":
    main()
    exit(0)