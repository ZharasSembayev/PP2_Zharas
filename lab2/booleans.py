"""
print(10 > 9)
print(10 < 9)
print(10 == 9)
print(10 >= 9)
"""

a = 300
b = 291
if a < b :
 print(" a is greater than b")
else :
    print ("b is greater than a")
    
"""
print(bool("Hello"))
print(bool(83))
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
"""
#FUNC
"""
class myclass():
  def __len__(self):
    return 1

zharas = myclass()
print(bool(zharas)) 

"""
def MyFunc():
    return True
if MyFunc():
    print("YES!!!")
else :
    print("NO!")    

"""
B Python также есть много встроенных функций,
которые возвращают логическое значение, например, функция,
которую можно использовать для определения того,
относится ли объект к определенному типу данных:isinstance()

x = 200
print(isinstance(x, int)) 
It s True
"""