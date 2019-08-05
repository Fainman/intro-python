"""
Strings and Collections

A string is an immutable sequence of Unicode code-points
"""

print('This is a string')
print("This is also a string")

# Concatenation and Adjacent Strings
s1 = "First"
s2 = "Second"
print(s1 + s2)

# Multi-line Strings and Newlines
s3 = """This is 
a multi-line 
string"""
print(s3)

s4 = "This is\na multi-line\nstring"
print(s4)

# Support for backslash
s5 = "A\244 in a string"
print(s5)

s6 = 'this is " wow'
print(s6)

# Raw Strings
raw_string = r'C:\User\Documents\Books'

# String as sequence
s = "parrot"
print("s[4]", s[4], type(s))

# Capitalize the string
print(s, s.capitalize())

