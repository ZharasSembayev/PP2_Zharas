#print("Hello")
#print('hello world!')

import sys
#print(sys.version)

#if 5 > 2:
 #print ("Five is greater than two!")   
#if 5 < 8:
 #print ("Five is less than eight!")
x = 5
z = "Zharas"
#print(x)
#print(z)

#Если вы хотите указать тип данных переменной, это можно сделать с помощью приведения.
#For example: x = str("5") , y = int(88) , z = float(43)

#Получить Тип:
#Вы можете получить тип данных переменной с помощью функции.type()
x = 5  
y = "Zharas" 
z = 47.2
print((x, y, z))
#print(type(x))

Almaty = ["Beauty", "Bigger", "Hometown"]
x = y = z = Almaty
#print(x)
#print(y)
#print(z)

x = "awesome"
def Myfunc():
    x = "best language"
    print("Python is " + x)
Myfunc()
print("Python is " + x)

"""
Тип текста:	str
Числовые типы:	int, , floatcomplex
Типы последовательности:	list, , tuplerange
Тип картографирования:	dict
Типы наборов:	set, frozenset
Булев тип:	bool
Бинарные типы:	bytes, , bytearraymemoryview
Тип "Нет":	NoneType

###

Example:	           Data Type:	
x = "Hello World"	   str	
x = 20	               int	
x = 20.5	           float	
x = 1j	               complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	       range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	           bool	
x = b"Hello"	       bytes	
x = bytearray(5)	   bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	           NoneType

"""

import random 
print(random.randrange(1,9))