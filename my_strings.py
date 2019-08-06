"""
Explore Strings
"""


def main():
    """
    Test function
    :return: 
    """
    s1 = "This is super cool"
    print("Size of s1", len(s1))
    # Concatenation "+"
    s2 = "Weber" + "State" + "University"
    print(s2)
    # If you need to join large strings, use the join() method
    # instead of the + operator
    teams = ["Real Madrid", "Barcelona", "Manchester United"]
    record = ":".join(teams)
    print(record)
    print(record.split(":"))
    # Partitioning Strings
    departure, separator, arrival = "London:Edinburgh".partition(":")
    print(departure, separator, arrival)
    departure, _, arrival = "London:Edinburgh".partition(":")
    print(departure, arrival)
    t = "London:Edinburgh".partition(":")
    print(t, type(t))
    # String formatting using format()
    print("The age of {0} is {1}".format("Mario", 34))
    print("The age of {0} is {1}, and the birthday of {0} is {2}".format("Mario", 34, "August 12th 1985"))
    # Omitting the index
    print("The age of {} is {}".format("Mario", 34))
    # By field name
    print("Current position {latitude} {longitude}".format(latitude="60 N", longitude="5 E"))
    print("Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=(85.6, 23.3, 99.0)))
    # Second version of "format": print(f"{var}") -- Supported in Python 3.7+


if __name__ == "__main__":
    main()
    exit(0)