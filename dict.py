"""

Learn about dictionaries. Probably used the most.
Dictionaries maps keys to values.

In some languages are known as associative arrays, or hashes, maps

Create them using {} containing a key-value pair
Retrieve them by key value
"""

d = {'alice': '878-8728-922',
     'bob': '256-5262-124',
     'eve': '198-2321-787'}
print(d, type(d))

# Access one element
print(d['bob'])

roster = {}
total = 0
while total < 3:
    # Get key value
    name = input("Enter player name")
    # Get value associated to key
    score = input("Enter score")
    # Add element to dictionary.
    # Note: If key value exists , it will update the value
    #    otherwise it will add it to the dict.
    roster[name] = score
    total += 1
print(roster)
