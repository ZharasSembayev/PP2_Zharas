x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(3, 8))

#Сила лямбда лучше проявляется, когда вы используете их как анонимные функция внутри другой функции.

def myfunc(n):
    return lambda a : a * n
func2 = myfunc(2)
func3 = myfunc(23)
print(func2(17))
print(func3(1))