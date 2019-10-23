# 2 kinds of loops (for and while)

a = 0
b = 0

# runs only when its conditions are met
while a == b:
  print("a equal b")

# can also be used to run forever
while True:
  print("this code runs forever")

# runs until index = 10
for index in range(10):
  # we can use the variable index while the code loops
  print(index)
