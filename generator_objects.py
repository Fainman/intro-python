"""
Generator objects are a cross between comprehensions and generator functions
Syntax: Similar to a list comprehension, but with parenthesis:
    (expr(item) for the item in teh iterable)
"""
from list_comprehensions import is_prime

def main():
    """
    Test function
    :return: 
    """
    m_sq = (x*x for x in range(1, 1000001))
    print(m_sq, type(m_sq))
    print('The sum of the first 1M squares is:', sum(x*x for x in range(1, 1000001)))
    print('The sum of the primes within the first 1M numbers is:', sum(x for x in range(1, 100001) if is_prime(x)))


if __name__ == '__main__':
    main()
    exit(0)