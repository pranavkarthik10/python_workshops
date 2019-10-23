# if statements are the core of computer programming

a = 1
b = 0

x = 1
y = 10

#remember to use double = signs in your if statements
if a == b: # : symbol is used to close the statement
  print("a is equal to b") # indented code runs when the if stetment is true

# use a ! followed by an = to run the if statement if the statement is not true
if a != b:
  print("a is not equal to b")

# use 'and' to tell the computer to run the code only if both conditions are true
if a != b and x == y:
  print("a is not equal to b and x is equal to y")
  
# use 'or' to tell the computer to run the code if either of the conditions are true
if a == b or x == y:
  print("either a = b or x = y")
  
# attach an 'else' at the bottom of your statement to run code when the statement is not true

if a == b:
  print("a = b")
else:
  print("this runs if a is not equal to b")
