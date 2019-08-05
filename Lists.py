"""
Learn about lists
Unlike strings,, lists are mutable.
You can update, and append elements to it
"""

l = [1, 2, 3]
print("Lists", l, type(l))
# A list of objects (any type)
a = ["apple", "orange", "pear"]
# Access by index notation
print(a, a[1])
# Replace an element
a[0] = "tomatoes"
print(a, a[1])


# Begin with an empty list
names = []
name = input("Enter your name. When done, type done\n")

while name != 'done':
    names.append(name)
    name = input("Enter your name. When done, type done\n")

print(names)
