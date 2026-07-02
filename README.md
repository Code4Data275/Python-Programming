# What is Python?
- Python is a popular programming language.
- It was created by Guido Van Rossum, and released in 1991.

### It is used for 
- web development (server-side)
- software development
- mathematics
- system scripting

## What can Python do?
- Python can be used on a server to create web applications.
- Python can be used alongside software to create workflows.
- Python can connect to database systems. It can also read and modify files.
- Python can be used to handle big data and perform complex calculations.
- Python can be used for rapid prototyping, or for production-ready software development.

## Why Python?
- Python works on different platforms (Windows, Mac, Linux, Raspberry Pi etc)
- Python has a simple syntax similar to the English Language.
- Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
- Python runs on an interpreter system, meaning the code can be executed as soon as it is written. This means that prototyping can be very quick.
- Python can be treated in a procedural way, an object oriented way or a functional way.

## Python Syntax compared to other programming languages
- Python was designed for readability, and has some similarities to the English language with influence from mathematics.
- Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
- Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

## Python Quickstart
- Python is an intepreted programming language, this means as a developer you write Python (.py) files in a text editor and then put those files into python interpreter to be executed.

## Python Command Line
- To test a short amount of code in python sometimes it is quickest and easiest not to write the code in a file. 
- This is made possible because Python can be run as a command line itself.

## Python Identation
- Indentation refers to the spaces at the beginning of a code line.
- Python uses identation to indicate a block of code.
- Python will give you an error if you skip the identation.
- The number of spaces is up to you as a programmer, the most common use is four, but it has to be atleast one.
- You have to use the same number of spaces in the same block of code, otherwise Python will give you an error.

## Statements
- A computer program is a list of instructions to be executed by the computer.
- In a programming language , these programming instructions are called statements.
- Most Python programs contain many statements.
- The statements are executed one by one, in the same order as they are written.

## Python Output
1. Print Text
    - We can use print() function to display text or output values.
    - You can use print function as many times you want. 
    - Each call prints text on a new line by default.
    - Text in Python can be inside quotes.
    - You can either use " double quotes or ' single quotes.
    - If you forget to put text inside quotes, Python will give you an error.
    - By default, the print() function ends with a new line.
    - If you want to print multiple words on the same line, you can use the end parameter.

2. Print Numbers
    - You can also use the print() function to display numbers.
    - However, unlike text, we don't put numbers inside double quotes.
    - You can also do math inside print() function

## Python Comments
- Comments can be used to explain the Python code.
- Comments can be used to make the code readable.
- Comments can be used to prevent execution when testing code.
- In Python, comments starts with #, and Python with ignore them.

## Python Variables
- Variables are containers for storing data values.
- Python has no command for declaring a variable.
- A variable is created the moment you first assign a value to it.
- Variables do not need to be declared with any particular type, and even can change type after they have been set.
- If you want to specify the data type of a variable, it can be done with casting.
- You can get the type of variable using the type() function
- Variable names are case-sensitive.
- A variable can have a short name or a more descriptive name
- Variables names with more than one word can be difficult to read.
- There are several techniques you can use to make them more readable:
    1. Camel Case:
        Each word, except first, starts with a capital letter.
    2. Pascal Case:
        Each word starts with a capital letter.
    3. Snake Case:
        Each word is separated by a underscore character.
- Python allows you to assign values to multiple variables in one line.
- You can also assign the same value to multiple variables in one line.
- If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
- The print() function is often used to output variables.
- Using print(), you can also separate multiple variables, separated by a comma.
- You can also use + operator to output multiple variables.
- For numbers, the + character works as a mathematical operator.
- In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
         
### Rules for naming a variable
- A variable name must start with a letter or a underscore character.
- A variable name cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )   
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords. 

## Global Variables
- Variables created outside of a function are known as global variables.
- Global variables can be used by everyone, both inside of functions and outside.
- If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
- The global variable with the same name will remain as it was, global and with the original value.

### Global keyword
- The global variable with the same name will remain as it was, global and with the original value.
- To create a global variable inside a function, you can use the global keyword.
- Also, use the global keyword if you want to change a global variable inside a function.

## Python Data Types
- In Programming, data type is an important concept
- Variables can store data of different types, and different types can do different things.

### Built-In Data Types
- Python has the following data types built-in by default, in these categories:
    - Text type: str
    - Numeric Types: int, float, complex
    - Sequence Types: list, tuples, range
    - Mapping Type: dict
    - Set Types: set, frozenset
    - Boolean: bool
    - Binary Types: bytes, bytearray, memoryview
    - None Type: NoneType

#### Getting the data type
- You can get the data type of any object by using the type() function.

#### Setting the data type
- In Python, the data type is set when you assign a value to a variable:

## Python Numbers
- There are three numeric types in Python:
    - int
    - float
    - complex
- Variables of numeric types are created when you assign a value to them.
- To verify the type of any object in Python, use the type() function.

1. Int
- Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

2. Float
- Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
- Float can also be scientific numbers with an "e" to indicate the power of 10.

3. Complex
- Complex numbers are written with a "j" as the imaginary part.

### Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods.

## Python Casting

### Specify a Variable Type
- There may be a times when you want to specify a type on to a variable.
- This can be done with casting.
- Python is an object-oriented language, as such as it uses classes to define data types, including its primitive types.
- Casting in Python is therefore done using constructor functions:
    - int() =>  constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
    - float() => constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
    - string() => constructs a string from a wide variety of data types, including strings, integer literals and float literals

## Python Strings
- Strings in Python are surrounded by either single quotation marks, or double quotation marks.
- 'hello' is same as "hello"
- You can display a string literal with the print() function.
- You can use quotes inside a string, as long as they don't match the quotes surrounding the string.
- Assigning a string to a variable is done with a variable name followed by an equal sign and the string.
- You can assign a multiline string to a variable by using three quotes.
- Like many other popular programming languages, strings in Python are arrays of unicode characters.
- However, Python does not have a character data type, a single character is simply a string with a length of 1.
- Square brackets can be used to access elements of the string.
- Since strings are arrays, we can loop through the characters in a string, with a for loop.
- To get the length of a string, we use the len() function.
- To check if a certain phrase or character is present in a string, we can use the keyword in.
- To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
- To Concatenate, or combine, two strings you can use the + operator.


### String Slicing
- You can return a range of characters by using the slice syntax.
- Specify the start index and the end index, separated by a colon, to return a part of string.
- The First character has index 0
- By leaving out start index, the range will start from the first character.
- By leaving out end index, the range will go to the end.
- Use negative indexes to start the slice from the end of the string.

### Modify Strings
- Python has a set of built-in methods that you can use on strings.
    1. Upper Case:
        - The upper() method returns the string in upper case.
    2. Lower Case:
        - The lower() method returns the string in lower case.
    3. Remove Whitespace:
        - Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
        - The strip() method removes any whitespace from the beginning or the end
    4. Replace String:
        - The replace() method replaces a string with another string.
    5. Split String:
        - The split() method returns a list where the text between the specified separator becomes the list items.

### String Format
- As we learned in the Python Variables chapter, we cannot combine strings and numbers.
- But we can combine strings and numbers by using f-strings or the format() method.

    1. F-Strings
        - F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
        - To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
        - A placeholder can contain variables, operations, functions, and modifiers to format the value.
        - A placeholder can include a modifier to format the value.
        - A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
        - A placeholder can contain Python code, like math operations.

### Escape Character
- To insert a character that are illegal in a string, use an escape character.
- An escape character is a backslash \ followed by the character you want to insert.
- An example of an illegal character is a double quote inside a string that is surrounded by double quotes
- To fix this problem, use the escape character \".

## Python Booleans
- Booleans represent one of two values: True or False.
- In programming you often need to know if an expression is True or False.
- You can evaluate any expression in Python, and get one of two answers, True or False.
- When you compare two values, the expression is evaluated and Python returns the Boolean answer.
- When you run a condition in an if statement, Python returns True or False
- The bool() function allows you to evaluate any value, and give you True or False in return.
- Almost any value is evaluated to True, if it has some sort of content
- Any string is True, except empty strings.
- Any number is True, except 0.
- Any list, tuple, set, and dictionary are True, except empty ones.
- In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
- One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False.
- You can create functions that returns a Boolean Value
- You can execute code based on the Boolean answer of a function
- Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type

## Python Operators
- Operators are used to perform operations on variables and values.
- Python divides the operators in the followin groups:
    1. Arithmetic Operators:
        - Arithmetic operators are used with numeric values to perform common mathematical operations:
            - +: Addition
            - -: Subtraction
            - *: Multiplication
            - /: Division
            - %: Modulo Division
            - **: Exponentiation
            - //: Floor Division
        - Python has two division operators:
            - / -> Division (returns a float)
            - // -> Floor division (returns an integer)
    2. Assignment Operators:
        - Assignment operators are used to assign values to variables:
            - =
            - +=
            - -=
            - *=
            - /=
            - %=
            - **=
            - //=
        - Walrus Operator: 
            - Python 3.8 introduced the := operator, known as the "walrus operator". 
            - It assigns values to variables as part of a larger expression.
    3. Comparison Operators:
        - Comparison operators are used to compare two values:
            - ==: Equal
            - !=: Not equal to
            - > : Greater than 
            - < : Less than
            - >=: Greater than or equal to
            - <=: Less than or equal to
        - Comparison operators return True or False based on the comparison
        - Python allows you to chain comparison operators
    4. Logical Operators:
        - Logical operators are used to combine conditional statements:
            - and: returns true if both conditions are true
            - or: returns true if either one of the condition is true
            - not: reverses the result, returns false if the condition is true
    5. Identity Operators:
        - Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
            - is: returns True if both variables are the same object
            - is not: returns True if both variables are not the same object
        - is: checks if both variables point to the same object in memory
        - ==: checks if the values of both variables are equal
    6. Membership Operators:
        - Membership operators are used to test if a sequence is presented in an object:
            - in: returns True if a sequence with the specified value is present in the object
            - not in: returns True if a sequence with the specified value is not present in the object
        - The membership operators also work with strings.
    7. Bitwise Operators:
        - Bitwise operators are used to compare (binary) numbers:
            - & (AND): Sets each bit to 1 if both bits are 1
            - | (OR): Sets each bit to 1 if one of two bits is 1
            - ^ (XOR): Sets each bit to 1 if only one of two bits is 1	
            - ~ (NOT): Inverts all the bits
            - >> (Signed right shift): Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
            - << (Zero right shift): Shift left by pushing zeros in from the right and let the leftmost bits fall off
    8. Ternery Operator:
        - The ternary operator allows one value if a condition is true, and another if it is false.
        - The ternary operator can be used instead of elif in longer if statements.
        



    