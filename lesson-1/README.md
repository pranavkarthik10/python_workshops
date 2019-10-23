# Lesson 1
## Data Types and Variables

We can print words into our console:
```python
  print("hello world")
```

Note that quotes mark a string (a list of characters and letters):
```python
  "hello world"
```

We can also print integers (no quotes):
```python
  print(123)
```

We can also and floats (no quotes, with a decimal):
```python
  print(123.45)
```

And we can do math with these numbers:
```python
  print(1 + 2 * 3 / 4 - 5)
```

Sometimes, we want to store data for later use. We do this with variables:
```python
  a = 5
  b = 6
  c = "Hello World"
  print(a + b)
  print(c)
```

We can also take inputs from a user, and store them in a variable:
```python
  a = input()
  print(a)
```

We can convert strings to numbers, and numbers to strings with the `int()` and `str()` functions:
```python
  a = int("123")
  b = str(123)
  print(a)
  print(b)
```

## Homework

### Write a program that takes in the height and width of a triangle, and prints out the area.
* Must ask user for input (as in the computer prints: “Please enter width:”)
* The area of a triangle is (width * height) / 2
* Use the int() function to convert input to integer

### Solution
```python
w = int(input("Please enter the width: "))

h = int(input("Please enter the height: "))

print((w * h) / 2)
```

### What are the results obtained by the following programs:

#### 1
```python
  x = 1
  y = x
  x = 3
  print(x + y)
```

#### 2
```python
  a = 1
  a = 2
  print(a)
```

#### 3
```python
  four = 4
  five = 5
  print(four + five)
```

#### 4
```python
  x = 10
  y = 6
  y = y + 2
  z = x - y
  print(z)
```

#### 5
```python
  my_variable = '4'
  my_variable = 4
  my_variable = my_variable * 4
  print(my_variable)
```