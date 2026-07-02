# Arithmetic Operators
x = 20
y = 11

print("Arithmetic Operators")
print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x % y) # Modulo Division
print(x // y) # Floor Division
print(x ** 4) # exponentiation

# Assignment Operators

print("Assignment Operators")
x = 5
print(x)

x += 3 # Addition
print(x)

x -= 3 # Subtraction
print(x)

x *= 3 # Multiplication
print(x)

x /= 3 # Division
print(x)

x %= 3 # Modulo Division
print(x)
 
x //= 3 # Floor Division
print(x)

x **= 3 # exponentiation
print(x)

print("Bitwise Operators")
x = 5
x &= 3 # Bitwise AND
print(x)

x = 5
x |= 3 # Bitwise OR
print(x)

x = 5
x ^= 3 # Bitwise XOR
print(x)

x = 5 
x >>= 3 # Rightshift
print(x)

x = 5
x <<= 3 # Leftshift
print(x)

# Walrus Operator
numbers = [1, 2, 3, 4, 5]

if(count := len(numbers)) > 3:
    print(f"List has {count} numbers")

# Comparison Operator
x = 5
y = 3
print("Comparison Operators")
print(x == y) # Equal to
print(x != y) # Not equal to
print(x > y) # Greater than
print(x < y) # Less than
print(x >= y) # Greater than equal to
print(x <= y) # Less than equal to

# Chaining Comparison Operators
print(1 < x < 10)
print(1 < x and x < 10)

# Logical operators
x = 5

print(x < 10 and x > 0) # AND operator
print(x < 5 or x > 10) # OR operator
print(not(x > 3 and x < 10)) # NOT Operator

# Identity Operators
x = ["apple","banana"]
y = ["apple","banana"]
z = x

# is operator
print("Identity Operators")
print(x is z)
print(x is y)
print(x == y)

# is not operator
print(x is not y)

# Membership Operators
print("Membership Operators")

fruits = ["apple","banana","cherry"]

# in operator
print("banana" in fruits)
print("pineapple" in fruits)

# not in operator
print("banana" not in fruits)
print("pineapple" not in fruits)

name = "Aldous"
print("A" in name)
print("a" in name)
print("l" not in name)

# Bitwise Operators
print(6 & 3) # Bitwise AND
print(6 | 3) # Bitwise OR
print(6 ^ 3) # Bitwise XOR
 

