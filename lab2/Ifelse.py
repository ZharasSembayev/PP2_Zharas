a = 12 
b = 12
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")