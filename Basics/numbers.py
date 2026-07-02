x = 7 # int
y = 3.14 # float
z = 1j # complex

print(type(x))
print(type(y))
print(type(z))

# Integer
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(x,type(x))
print(y,type(y))
print(z,type(z))

#Complex
x = 3+5j
y = 5j
z = -5j

print(x,type(x))
print(y,type(y))
print(z,type(z))

# Type conversion
x = 7 # int
y = 3.14 # float
z = 1j # complex

a = float(x)
b = int(y)
c = complex(x)

print(a,type(a))
print(b,type(b))
print(c,type(c))

# Random number
import random
print(random.randrange(1,10))
