# list
countries = ["India","New Zealand","England","South Africa","Australia","Pakistan"]
print(countries) # Print the list
print(len(countries)) #Length of the list

fruits = ["apple","banana","cherry","apple","cherry"]
print(fruits,len(fruits))

list1 = ["Google","Microsoft","Amazon","Spotify"] # Strings
list2 = [10,20,30,23] # Numbers
list3 = [True,False,False,True] # Boolean

my_data = ["Aldous",22,"Bachelor in Science",7.72,True]
print(my_data)
print(type(my_data)) # type() func

# list() constructor
ipl_teams = list(("MI","RCB","CSK","KKR"))
print(ipl_teams)

# Accessing items
print(list1[3]) # 4th element
print(list1[2]) # 3rd element

# Negative Indexing
print(countries[-1]) # last element
print(countries[-2]) # second last element

# List Slicing
print(countries[2:5])
print(countries[:4])
print(countries[3:])
print(countries[-5:-1])

# in keyword
if "India" in countries:
    print("Yes, 'India' is present in the list")

# Change List items
countries[5] = "Sri Lanka"
print(countries)

countries[4:6] = ["Afghanistan","West Indies"]
print(countries)

countries[1:2] = ["Bangladesh","Ireland"]
print(countries)

countries[3:5] = ["Netherlands"]
print(countries)

countries.insert(3, "Zimbabwe")
print(countries)

# Add List Items
countries.append("Australia")
print(countries)
countries.insert(2,"South Africa")
print(countries)

lower_division_countries = ["USA","Nepal","Italy"]
countries.extend(lower_division_countries)
print(countries)

emerging_countries = ("Italy","Germany","France")
countries.extend(emerging_countries)
print(countries)

# Remove items
subjects = ["Physics","Mathematics","Chemistry","Computer Science","Chemistry"]
print(subjects)
subjects.remove("Chemistry") # remove() method
print(subjects)

subjects.pop(2) # pop() method
print(subjects)
subjects.pop()
print(subjects)

del subjects[0]
print(subjects)

subjects.clear()
print(subjects)

# Loop through the list
food = ["Noodles","Fried Rice","Lollipop","Crispy"]
# for loop
for x in food:
    print(x,end=" ")

# for loop using index value
for i in range(len(food)):
    print(food[i])

# while loop
i = 0
while i < len(food):
    print(food[i])
    i += 1

# List Comprehension
[print(x) for x in food]

# Without List Comprehension
fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# With list comprehension
a_fruits = [x for x in fruits if "a" in x]
print(a_fruits)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ["Aldous" for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# Sort Lists
## Ascending
thisList = ["Python","Java","C","C++","Javascript","Kotlin"]
thisList.sort()
print(thisList)

thisList = [100, 50, 65, 82, 23]
thisList.sort()
print(thisList)

## Descending
thisList = ["Python","Java","C","C++","Javascript","Kotlin"]
thisList.sort(reverse=True)
print(thisList)

thisList = [100, 50, 65, 82, 23]
thisList.sort(reverse=True)
print(thisList)

def myFunc(n):
    return abs(n - 50);

thisList.sort(key=myFunc)
print(thisList)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy a list
cricketing_nations = countries.copy()
print(cricketing_nations)

thisList = ["apple","banana","cherry","kiwi"]
myList = list(thisList)
print(myList)

theList = thisList[:]
print(thisList)

# Join a list
indian = ["Rohit Sharma", "Suryakumar Yadav", "Jasprit Bumrah","Hardik Pandya"]
overseas = ["Ryan Rickleton","Quinton DeKock","Will Jacks","Trent Boult"]
mumbai_indians = indian + overseas
print(mumbai_indians)

for x in overseas:
    indian.append(x)
print(indian)

indian.extend(overseas)
print(indian)