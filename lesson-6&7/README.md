# lesson 6/7
In this week’s python workshop, we learned two very important principles: list and string manipulation. these are possibly **the most important** principles in contest programming (and therefore the Canadian computing competition).

# What is string manipulation?
As we already know strings in programming are words (ie: “Hello”, “Goodbye”). We can use string manipulation to edit strings during runtime. For example, we can turn every “A” character in someone’s name into a “B”. Therefore turning “Andrei” into “Bndrei”. There are many parts to string manipulation, here are the most important.

### len()
A **VERY** important part of string manipulation is the len() method. len() returns the length of a string. For example, len(“Hello”) would return five.

Code:
```
Print(len(“hello”))
```
Output:
```
5
```

### index
We can access a particular character in a string using this syntax **variable[index]**. Variable obviously being the variable and index the position of the letter in the string.
(NOTE: the first letter in a string is indexed as 0)

Hello

01234

## letter replacer example
```
Name = “Andrei”
For I in range(len(Name)):
	If Name[i] == “A”:
		Name[i] = “B”
Print(Name)
```

# What are lists?
Lists in python are just like in real life, we can order variables and index them. For example, we could write a shopping list program. We can use all the tools from the string manipulation in our lists. The main difference between lists and strings is that lists can change their length during runtime (something that is very rare in other programming languages) and that lists can contain non string characters (such as numbers and other data structures)

Here our shopping list implemented
```
# shopping list
Shopping_list = [apple, cheese, milk]
# prints whole list
Print(Shopping_list)

# prints apple
Print(Shopping_list[0])
```

# Project
Now that we have all the tools available, we can create out first major project: The word reverser. Scroll down if you are having difficulties.






```

# note: there are way faster ways of reversing a string in python but you learn a lot more from this version
def ReverseString(string):

    newString = []
    stringLenght = len(string) - 1
    
    for i in range(stringLenght + 1):

        newString.append(string[stringLenght - i])

    return ''.join(newString)

print("String reversal program")
s = input("enter the string you want to reverse: ")

print(ReverseString(s))

    
```



> lesson paper by Andrei

