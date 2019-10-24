# Lesson 4
## Loops

Sometimes, we find ourselves repeating code:
```python
  print("hello world")
  print("hello world")
  print("hello world")
  print("hello world")
  print("hello world")
  print("hello world")
  print("hello world")
  print("hello world")
```

Instead of repeating ourselves, we can loop over code:
```python
  for x in range(1, 10):
    print("hello world")
```

We can use x inside the loop to get the how namy times the loop has looped:
```python
  for x in range(1, 10):
    print(x)
```

We can determine how many times a loop loops, and where it starts, by changing the paremeters of the range function:
```python
  for x in range(123, 456):
    print(x)
```

We can also use while loops:
```python
  i = 0
  while i < 10:
    i = i + 1
    print(i)
```

While runs while a condition is true.


## Homework

### Write a loop, that says all even numbers between 1 and 10
* Ifs can be used inside loops.
* The modulu (%) operator can be used to find the remainder of 2 numbers

### Solution
```python
  for i in range(1, 10):
    if i % 2 == 0:
      print(i)
```
