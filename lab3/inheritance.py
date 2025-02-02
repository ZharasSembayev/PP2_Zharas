#Наследование позволяет нам определить класс, который наследует все методы и свойства от другого класса

#Создание родительского класса:
#Любой класс может быть родительским классом, поэтому синтаксис такой же, как и при создании любого Другой класс:

#Создание дочернего класса:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
    
class student(Person):
    pass
x = student("Zharas", "Kulmeskhan")
x.printname()

#Чтобы сохранить наследование родительской функции, добавьте вызов к функции Функция родителя:
#Person.__init__(self, fname, lname)
   
"""
В Python также есть функция,
которая заставит дочерний класс наследовать все методы,
свойства от своего родитель:super()

"""
class adam:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def Any(self):
        print(self.name, self.age)

class Iam(adam):
    def __init__(self, name, age):
     super().__init__(name, age)
     self.year = 2007
a = Iam("Kulmeskhan", 18)
a.Any()
print(a.year)

    
#Добавим в класс вызываемое свойство:self.year = 2007
