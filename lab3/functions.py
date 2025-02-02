#Arguments
def Myfunc(fname):
    print(fname + " Zharas")
Myfunc("Sembayev ") #Для вызов функцию мы используем имя функции
Myfunc("Berikkazyevich ")
Myfunc("Muslim ")
#Термины parameter и argument можно использовать для одного и того же: информации, которая передается в функцию

#def func(fname, iname):
    #print(fname + " " + iname)
#func("Sembayev" , "Zharas")

#Если количество аргументов неизвестно, добавьте a перед именем параметра:*
#for example:
def func2(*youngs):
    print("The youngest person is " + youngs[1])
func2("Asan", "Zharas", "Arman")

#Вы также можете отправлять аргументы с помощью синтаксиса ключ = значение.
#Таким образом, порядок аргументов не имеет значения.

def func3(country = "Kaz"):
    print("I am from is " + country)
func3("Rus")
func3("Uzb")
func3()
func3("Ukr")

def func4(food):
    for x in food:
        print(x)
fruits = ["Apple", "Banana", "Watermelon"]
func4(fruits)

#Чтобы функция возвращала значение, используйте оператор:return 
def func5(x):
    return 7 * x
print(func5(2))
print(func5(3))
print(func5(4))

"""
    function определения не могут быть пустыми,
    но если У вас по какой-то причине есть определение без содержания,
    внесите в оператор, чтобы избежать получения ошибки.function pass
    
"""

def func6(a,b, /, *, c, d ):
    print(a + b + c + d)
func6(5, 3, c = 2, d = 4)

#Recursion:
def rec(k):
    if (k > 0) :
        result = k + rec(k-1)
        print(result)
    else:
        result = 0
    return result
print("Recursion Example Results:")    
rec(6)