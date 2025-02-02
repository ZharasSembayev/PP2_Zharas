#Чтобы создать класс, используем ключевое слово: class!
class myclass:
    x = 5
p1 = myclass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Zharas", 18)
print(p1.name)
print(p1.age)

class Adam:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Myfunc(self,):
        print("My name is " + self.name)
p1 = Adam("Kulmeskhan", 18)
p1.Myfunc()

#if you wanna change your old.
p1.age = 20
print(p1.age)

#Вы можете удалить свойства объектов с помощью ключевого слова: del
#Вы можете удалить объекты с помощью ключевого слова:del
del p1.age
print(p1.age)
        
class Person:
    pass       
    