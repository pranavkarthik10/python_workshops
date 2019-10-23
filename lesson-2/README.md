# Lesson 2
## Functions

We can call functions, such as print:
```python
  print("hello world")
```

We can also define our own functions:
```python
  def sayHi():
    print("hi")

  sayHi()
```

Things located in the parentheses are what the function gets:
```python
  def say(theThingIGet, numberIGet):
    print(theThingIGet)
    print(numberIGet)

  say("hello world", 123456789)
```

The name of the function is located after `def`:
```python
  def thing():
    print('what`s up')

  thing()
```

Functions can also return values:
```python
  def function():
    return "hello world"

  print(function())
```

## Homework

### Write a function to find the area of a circle using the radius. Then ask the user to input a radius. Print the area of the circle.
* (pi)(r)^2 is the area of a circle.

### Solution
```python
def calculateArea(r):
  pi = 3.14
  return pi * r * r

radius = int(input("Enter radius: "))

print("The area of the circle is:")
print(calculateArea(radius))
```
