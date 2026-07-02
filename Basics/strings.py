print("Hello")
print('Hello')

# Quotes inside string
print("It's sunny today")
print("My name is 'Aldous Dsouza'")
print('I live in "Goa"')

# Assigning a variable to a string
name = "Aldous"
print(name)

# Multiline Strings
a = """
    Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.
"""
print(a)

# String as arrays
country = "India"
print(country[1])
print(country[3])

# Looping through a string
for x in "Mumbai":
    print(x,end=" ")

# Length of the string
a = "Mumbai"
print(len(a))

# Check String

# using in keyword
text = "The best things in life are free!" 
print("free" in text)

# using if statement
if "free" in text:
    print("Yes, 'free' is present")

# Check if NOT

# using in
print("expsensive" in text)
print("expsensive" not in text)

# using if statement
if "expensive" not in text:
    print("No, 'expensive' is NOT present.")

# String slicing
company = "Google"
print(company[1:3])
print(company[2:5])
print(company[:4]) # Slice from the start
print(company[3:]) # Slice to the end
print(company[-4:-2]) # Negative indexing
print(company[-2:])

# Modify strings
city = "Mumbai"
print(city.upper()) # upper case
print(city.lower()) # lower case
print(" Aldous ".strip()) # remove whitespace
print(city.replace('M','B')) # replace string
print(city.split('m')) # Split String

firstName = "Aldous"
lastName = "Dsouza"
fullName = firstName + " " + lastName
print(fullName)

# Format Strings
name = "Aldous"
age = 21
print(f"My name is {name} and I'm {age} yrs old")

price = 50000
product = "Playstation"
print(f"This {product} costs ₹. {price:.2f}")

print(f"5 x 5 = {5 * 5}")

# Escape Character
txt = "We are so called \"Indians\" from Asia"
print(txt)

