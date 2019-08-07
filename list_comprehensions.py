"""
List Comprehensions

"""
from math import factorial
from math import sqrt
from pprint import pprint as pp

def main():
    """
    Test function
    :return: 
    """
    data = []
    words = "Today I am very happy to learn about list comprehensions".split()
    print(words)
    for word in words:
        # Some analysis
        data.append(word)
        print(word)
    # "Filter" data
    print(data)

    # Task: Find the length of the first 20 factorial numbers
    solution = []
    for x in range(20):
        print(factorial(x))
        solution.append(len(str(factorial(x))))
    print(solution)

    # Use a list comprehension instead: [ ]
    info2 = [len(str(factorial(x))) for x in range(20)]
    pp(info2)

    # Set Comprehensions: { } - removes duplicates
    info3 = {len(str(factorial(x))) for x in range(20)}
    pp(info3)

    # Dictionary Comprehensions { }
    nba_teams = {'Jazz': 'SLC', 'Warriors': 'OAKLAND', 'Lakers': 'LA', 'Clippers': 'LA'}
    teams_nba = {city: mascot for mascot, city in nba_teams.items()}
    pp(teams_nba)

    # Filter predicates
    primes = [x for x in range(101) if is_prime(x)]
    print(primes)
    print(len(primes), primes)


def is_prime(num):
    """
    Determine if the number is prime
    :param num: number to test
    :return: True for prime; False for non-prime numbers
    """
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()
    exit(0)