# print("Hello Python")

# Scalar data types: Integers, Floating point
# None, and Boolean

print("Binary Notation", 0b0100)
print("Hex Notation", 0x0100)

# use the int() constructor
int("477")

# Option for base
print(int("1001", 2))

# Floating point: IEEE-754 notation
x = 3.7
print("Type", type(x))
print("Scientific notation", 1.61e-35)

# Boolean
print("Boolean const. bool()", bool(0))
print("Boolean const. bool(42)", bool(42))
print("Boolean const. bool(.1)", bool(.1))
print("Boolean const. bool([])", bool([]))
print("Boolean const. bool([1,2,3])", bool([1, 2, 3]))
print("Boolean const. bool('False')", bool("False"))