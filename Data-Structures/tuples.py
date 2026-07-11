thisTuple = ("apple","banana","mango")
print(thisTuple)

# Tuples allow duplicate values
fruits = ("apple","mango","cherry","banana","mango","apple")
print(fruits)

# length of the tuple
print(len(thisTuple))
print(len(fruits))

thisTuple = ("Virat")
print(type(thisTuple))

thisTuple = ("Virat",)
print(type(thisTuple))

tuple1 = ("apple","banana","mango") # string tuple
tuple2 = (12,14,15,23) # int tuple
tuple3 = (True, False, False, True) # boolean tuple
tuple4 = ("Virat",18,"Rohit",45) # Mixed Tuple
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

languages = tuple(("Python","Java","C","C++"))
print(languages)

# Access Items 
print(languages[2]) # 3rd element
print(languages[1]) # 2nd element
# Negative Indexing
print(languages[-1]) # Last element
print(languages[-3]) # 3rd Last Element

# Range Slicing
teams = ("MI","RCB","CSK","KKR","GT","SRH","PBKS","DC","LSG","RR")
print(teams[2:5])
print(teams[3:4])
print(teams[1:9])
print(teams[:3])
print(teams[:6])
print(teams[2:])
print(teams[4:])
print(teams[5:])
print(teams[-3:-1])
print(teams[-4:-2])
print(teams[1:9:3])
print(teams[:-1:2])

if "GT" in teams:
    print("Yes, GT is among IPL teams")

# Change item
x = ("Java","C++","Python","Kotlin")
print("Before updating:",x)
y = list(x)
y[1] = "C"
x = tuple(y)
print("After updating:",x)

# Add items
y = list(x)
y.append("Dart")
x = tuple(y)
print(x)

# Add tuple to tuple
z = ("Go","Rust","R","Javascript")
x += z
print(x)

# Remove items
y = list(x)
y.remove("Kotlin")
x = tuple(y)
print(x)

# Completely delete tuple
del x

# Unpacking
fruits = ("apple","banana","cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple","mango","pineapple")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# Looping
for x in fruits:
    print(x, end=" ")

for x in range(len(fruits)):
    print(fruits[x], end=" ")

i = 0
while i < len(fruits):
    print(fruits[i], end=" ")
    i += 1

# Join Tuples
players = ("Virat", "Rohit", "Jasprit", "Rahul", "Rishabh")
numbers = (18, 45, 93, 1, 17)
player_numbers = players + numbers
print("\n",player_numbers)

myTuple = players * 3
print(myTuple)

# Tuple methods
fruits = ("apple","banana","cherry","banana")
print(fruits.count("apple"))
print(fruits.index("banana"))
