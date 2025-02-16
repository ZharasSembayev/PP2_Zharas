#Доступ к локальной переменной можно получить из функции внутри функции:
def myfunction():
    x = 300
    def func2():
        print(x)
    func2()
myfunction()

x = 500
def func3():
    x = 200
    print(x)
func3()
print(x)

#Ключевое слово делает переменную глобальной: global x
#Ключевое слово используется для работы с переменными внутри вложенных функций: nonlocal x

def function4():
    x = "Zharas"
    def func5():
        nonlocal x
        x = "Hello"
    func5()
    return x 
print(function4())