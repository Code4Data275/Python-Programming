thisset = {"apple", "cherry","banana"}
print(thisset)
print(len(thisset))

thisset = {"apple","banana","cherry","apple"}
print(thisset)
print(len(thisset))

thisset = {"apple", "banana", "cherry", True, 1, 2, 0, False}
print(thisset)

print(len(thisset))

set1 = {"apple", "banana", "cherry"} # string
set2 = {1, 5, 7, 9, 3} # int
set3 = {True, False, False} # boolean
print(set1)
print(set2)
print(set3)

set4 = {"abc", 12, True, 40, "male"}
print(set4)

print(type(thisset))

cars = set(("Kia","Tiago","Honda","Harrier"))
print(cars)
print(len(cars))
print(type(cars))

for x in cars:
    print(x, end=" ")
print("\n")
print("Kia" in cars)
print("Kia" not in cars)
print("BMW" in cars)
print("BMW" not in cars)

cars.add("BMW")
print(cars)

programming_languages = {"Java","C++","Python","Javascript"}
frameworks = {"React.js","NodeJS","ExpressJS","Flask","Spring boot"}
programming_languages.update(frameworks)
print(programming_languages)

product = {"Google", "Microsoft", "Amazon"}
service = ["Infosys", "Accenture"]
product.update(service)
print(product)

product.remove("Infosys")
print(product)
cars.remove("Honda")
print(cars)

product.discard("Accenture")
print(product)
cars.discard("Tiago")
print(cars)

x = product.pop()
y = cars.pop()
print(x)
print(y)
print(product)
print(cars)

product.clear()
print(product)

del product

fruits = {"apple","banana","mango","cherry"}
for x in fruits:
    print(x)

# Joining sets
# 1. Union

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = set1.union(set2)
print(set4)

set5 = {"Virat", "Rohit"}
set6 = {"apple", "banana", "mango"}
myset = set1.union(set1, set2, set5, set6)
print(myset)

my_set = set1 | set2 | set5 | set6
print(my_set)

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# 2. Intersection

set1 = {"apple","banana","cherry","mango"}
set2 = {"grapes","mango","apple","guavas"}
set3 = set1.intersection(set2)
print(set3)

set4 = set1 & set2
print(set4)

set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# 3. Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
set4 = set1 - set2
print(set3)
print(set4)

set1.difference_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
set4 = set1 ^ set2
print(set3)
print(set4)

set1.symmetric_difference_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple", "banana", "cherry"}

print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set2.issuperset(set1))

# frozen set
x = frozenset({"Google","Infosys","Capgemini","Accenture"})
print(x)
print(type(x))

c = x.copy()
print(c)

x = frozenset({"RCB","MI","PBKS","GT"})
y = frozenset({"RCB","GT","RR","SRH"})

print(x.difference(y))
print(x.intersection(y))
print(x.isdisjoint(y))
print(x.issubset(y))
print(x.issuperset(y))
print(x.symmetric_difference(y))
print(x.union(y))