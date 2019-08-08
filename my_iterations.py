"""
When working with iterators, generators, etc
Look at the documentation for the itertools module
"""
from itertools import islice, count, chain
from list_comprehensions import is_prime
import statistics



def main():
    """
    Test function
    :return: 
    """
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes, type(thousand_primes))
    print("List of first 1K prime numbers:", list(thousand_primes))
    # Note: If you need to use the object again, you need to re-generate it
    print(thousand_primes, type(thousand_primes))
    print("List of first 1K prime numbers:", sum(thousand_primes))
    # Other built-ins use with itertools: any ("or"), all ("and")
    print(any([False, False, True]))
    print(all([False, False, True]))
    print("There are prime numbers between 1328 and 1361:", any(is_prime(x) for x in range(1328, 1362)),
          list(x for x in range(1328, 1362) if is_prime(x)))
    # Check if all names in an iterable are in title form: First letter capitalized
    names = ["London", "New York", "Ogden"]
    print(all(name == name.title() for name in names))
    # Another built-in: zip()
    monday = [12, 14, 14, 15, 15, 16, 15, 13, 10, 9]
    tuesday = [13, 14, 15, 15, 16, 17, 16, 16, 12, 12, 1] # Zip works on the min length of inputs
    wednesday  = [12, 14, 11, 12, 15, 16, 15, 10, 9, 9]
    # Calculate the min, max, and avg of all points
    for item in zip(monday, tuesday, wednesday):
        print("Min = {:4.1f}, Max = {:4.1f}, Avg = {:4.1f}".format(min(item), max(item), sum(item)/len(item)))
        print("Min:", min(item))
        print("Max:", max(item))
        print("Avg:", statistics.mean(item))
    # Chain
    all_temps = chain(monday, tuesday, wednesday)
    print(all_temps, type(all_temps))
    print("All temperatures > 0", all(t > 0 for t in all_temps))


if __name__ == '__main__':
    main()
    exit(0)