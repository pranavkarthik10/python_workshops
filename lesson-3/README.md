# Lesson 3
## Decision Making

Decision making in Python is just the same as decision making in real life.

Let's take weather as an example. In real life if it rains outside you would take an umbrella, if not then you wouldn't

In python it's pretty similar:
```python
  weather = "rain"
  if weather == "rain":
      print("Take an umbrella!")
  else:
      print("Don't take an umbrella.")
```

You use if + the statement + : to declare an if statement.
Don't forget the colon!

Else is the same but without any statement.

There's also elif for when you have multiple options.

For example:
```python
  age = 34
  if age < 7:
      print("kid")
  elif age < 18:
      print("teen")
  else:
      print("adult")
```

This can save time and be more compact.