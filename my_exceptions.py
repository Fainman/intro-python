"""
Learn about exceptions
"""
import sys


def convert(s):
    """
    Converts a string to integer
    :param s: input string
    :return:
    """
    try:
        return int(s)
    except (TypeError, ValueError) as e:
        print("Conversion error {}"\
              .format(str(e)), file=sys.stderr)
        # print("Conversion failed!")
        # x = -1
    return -1


def main():
    """
    Test function
    :return: 
    """
    print(convert('11'))
    print(convert('Hello'))
    print(convert([1, 4, 8]))


if __name__ == "__main__":
    main()
    exit(0)