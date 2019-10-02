# Lesson #1 - Variables + Type Conversion

# Variables are data that can change
# You can use them to store and modify data such as strings, integers, floats, and booleans

# Declare a variable like this - (identifier) = (value)

# eg.
a = 5
b = "Hello World!"
c = true

# We can print our variables or use them for operations

print(a)
print(b)

x = a + 32
print(x)

# You can also add strings together

starter = "My name is "
name = "Bob"
print(starter + name)

# But what if you wanted to print a string with an integer?
# You need to convert your integer to a string

# eg.
print("I am " + str(14) + " years old")

# You can do this with floats too
print("People in this room: " + str(30.0))


# If there's time
# Let's say you wanted to get user input and use that in your output

# You can get input like this
u = input("What is your name? ")
print("Hi " + u)
