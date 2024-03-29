"""
Learn Dictionaries
"""


from pprint import pprint as pp


def main():
    """
    Test function
    :return: 
    """
    urls = {
        "google": "www.google.com",
        "yahoo": "www.yahoo.com",
        "twitter": "www.twitter.com",
        "wsu": "www.weber.edu"
    }
    print(urls, type(urls))
    # Access by key: [key]
    print(urls["wsu"])
    # Build dict with dict() constructor
    names_age = [('Alice', 32), ('Mario', 23), ('Hugo', 21)]
    d = dict(names_age)
    print(d)
    # Another method
    phonetic = dict(a='alpha', b='bravo', c='charlie', d='delta')
    print(phonetic)
    # make a copy
    e = phonetic.copy()
    print(e)
    # Updating a dictionary
    stocks = {'GOOG': 891, "AAPL": 416, 'IBM': 194}
    print(stocks)
    stocks.update({'GOOG': 999, "YHOO": 2})
    print(stocks)
    # Iteration default is by key
    for key in stocks:
        print("{k} => {v}".format(k=key, v=stocks[key]))
    # Iterate by values
    for val in stocks.values():
        print("val = {v}".format(v=val))
    # Iterate by both key and value with: items()
    for name, value in stocks.items():
        print(name, value)
    # test for membership
    print('GOOG' in stocks)
    print('WINDOWS' not in stocks)
    # Deleting: del keyword
    print(stocks)
    del stocks['YHOO']
    print(stocks)
    # Mutability of dictionaries
    isotopes = {
        'H': [1, 2, 3],
        'He': [3, 4],
        'Li': [6, 7],
        'Be': [7, 9, 10],
        'B': [10, 11],
        'C': [11, 12, 13, 14]
    }
    print(isotopes)
    isotopes['H'] += [4, 5, 6, 7]
    print(isotopes)
    isotopes['N'] = [13, 14, 15]
    print(isotopes)
    pp(isotopes)


if __name__ == "__main__":
    main()
    exit(0)