import sys
#print(sys.version)

#Если вы хотите указать тип данных переменной, это можно сделать с помощью приведения.
#For example: x = str("5") , y = int(88) , z = float(43)

#Получить Тип:
#Вы можете получить тип данных переменной с помощью функции.type()
x = 5  
y = "Zharas" 
z = 47.2
print((x, y, z))
#print(type(x))

x = "awesome"
def Myfunc():
    x = "best language"
    print("Python is " + x)
Myfunc()
print("Python is " + x)

"""
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
"""

import random 
print(random.randrange(1,9))

#Создайте итератор, возвращающий числа, начиная с 1, и каждую последовательность увеличится на единицу:
class myclass:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
class2 = myclass()
stre = iter(class2)
print(next(stre))
print(next(stre))
print(next(stre)) 
print(next(stre))

#Остановка после 20 итераций:
class myclass2:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
class3 = myclass2()
myiter = iter(class3)
for x in myiter:
    print(x) # end = " "

#Импортируйте модуль datetime и отобразите текущую дату:
import datetime
i = datetime.datetime.today()
print(i)

#Верните год и название дня недели:
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#Создадим объект даты:
x = datetime.datetime(2025, 3, 6)
print(x)

import math 
x = math.floor(1.4)
y = math.ceil(1.4)
print(x,y)

#1:который генерирует квадраты чисел с точностью до некоторого числа:
def generator(N):
    for i in range(1, N+1):
        yield i ** 2
Mygenerator = generator(5)
for x in Mygenerator:
    print(x)
    
#2:для вывода четных чисел от 0 до запятых через запятую:
def generator2(n):
    for i in range(0, n+1, 2):
        yield i
n = int(input("n = "))
mygenerator = generator2(n)
print(",".join(map(str, mygenerator)))

#3:которая может перебирать числа, кратные 3 и 4, между заданным диапазоном от 0 до N:
def generator3(n):
    for i in range(0, n+1, 12):
        yield i 
n = int(input("n = "))
my = generator3(n)
print(",".join(map(str, my)))

#4:вызываемый для получения квадрата всех чисел от (n) до (N).
def generator4(n, N):
    for i in range(n, N+1):
        yield pow(i,2)
n = int(input("n= "))
N = int(input("N= "))
my = generator4(n, N)
print(",".join(map(str, my)))

#5: который возвращает все числа от (n) до 0.
def generator5(n):
    for i in range(n,-1,-1):
        yield i 
n = int(input("n= "))
my = generator5(n)
for x in my:
    print(x)
    
#Data:
#1:для вычитания пяти дней из текущей даты.
import datetime 
today = datetime.datetime.today()
l = today - datetime.timedelta(days=5)
print(l.strftime("%Y-%m-%d")) 

#2:чтобы печатать вчера, сегодня, завтра.
today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days = 1)
print(today.strftime("%Y-%m-%d"))
print(yesterday.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))

#3:чтобы отбрасывать микросекунды от даты и времени.
t = datetime.datetime.now()
print(t.strftime("%Y-%m-%d, %H:%M:%S"))

#4:для вычисления разницы в две даты за секунды.
date1 = input()
date2 = input()
format = ("%Y-%m-%d %H:%M:%S")
dt1 = datetime.strptime(date1, format)
dt2 = datetime.strptime(date2, format)
diff = abs((dt2 - dt1).total_seconds())
print(diff)

#MATH:
#1:для преобразования градуса в радиан:
import math 
d = int(input())
r = math.radians(d)
print(r)

#JSON:
import json
data = {
    "Name":"Zharas",
    "age":18,
    "City":"Almaty",
    "Univer":"KBTU",
    "Profession":"IS"
}
json_str = json.dumps(data, indent=4)
print(json_str)


