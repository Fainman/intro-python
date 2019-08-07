"""
Program to simulate 6000 rolls of a die (1-6)
"""

import random
import statistics


def roll_die(num):
    """
    Random roll of a die
    :param num: number of rolls
    :return: a list of frequencies
    Index 0 maps to 1
    .
    .
    .
    Index 5 maps to 6
    """
    frequency = [0] * 6  # Initial values to 0
    for i in range(6000):
        roll = random.randint(1, 6)
        frequency[roll - 1] += 1
    return frequency


def main():
    """
    Test function
    :return: 
    """
    num = int(input("How many times do you need to roll? "))
    result = roll_die(num)
    print(result)
    for roll, total in enumerate(result):
        print(roll+1, total)
    mean = sum(result)/len(result)
    print("Average = {}".format(mean))
    print("Mean = {}".format(statistics.mean(result)))


if __name__ == "__main__":
    main()
    exit(0)