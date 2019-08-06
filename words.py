"""
Get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task 1: Count number of words in document
"""

from urllib.request import urlopen
file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"


def word_frequency(file_location):
    """
    Prints number of each word from file
    :param file_location: Website of text file
    :return:
    """
    count = 0
    data = {}
    with urlopen(file_location) as story:
        for line in story:
            words = line.decode('utf-8').split()
            for word in words:
                count += 1
                if word in data:
                    data[word] += 1
                else:
                    data[word] = 1
        for key in sorted(data.keys()):
            print(key, data[key])


def fetch_words(file_location):
    """
    Prints number of each word from file
    :param file_location: Website of text file
    :return: a list with the items
    """
    count = 0
    data = []
    with urlopen(file_location) as story:
        for line in story:
            words = line.decode('utf-8').split()
            for word in words:
                data.append(word)
    return data


def main():
    """
    Test function for words library
    :return: nothing
    """
    word_frequency(file)
    words = fetch_words(file)
    print_words(words)


def print_words(items):
    """
    Print elements of the list
    :param items: A collection of objects
    :return: nothing
    """
    for item in items:
        print(item)


if __name__ == "__main__":
    print(__name__)
    main()
    exit(0)


