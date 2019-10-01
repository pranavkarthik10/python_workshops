# Homework
Write a function to find the area of a circle using the radius. Then ask the user to input a radius. Print the area of the circle.
   * (pi)(r)^2 is the area of a circle.

# Solution
```python
def calculateArea(r):
  pi = 3.14
  return pi * r * r

radius = int(input("Enter radius: "))

print("The area of the circle is:")
print(calculateArea(radius))
```
