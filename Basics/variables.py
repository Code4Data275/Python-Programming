x = 21 # x is of type int
y = "Aldous" # y is of type string
print(x)
print(y)

#Casting
x = str(3)
y = int(3)
z = float(3)
print(x,y,z)

# Get the type of variable
print(type(x))
print(type(y))
print(type(z))

# many values to multiple variables
x, y, z = "Virat", "Rohit", "Jasprit"
print(x)
print(y)
print(z) 

# one value to multiple variables
x = y = z = "India"
print(x)
print(y)
print(z)

# unpacking
companies = ["Google","Microsoft","Meta"]
a, b, c = companies
print(a)
print(b)
print(c)