cars = ["Camry", "Lexus" , "BMW"]
print(cars)

#Массив — это специальная переменная, которая может содержать более одного значения одновременно.

#Получим значение первого элемента:
x = cars[0]
print(x)

#Изменяем значение 3 го элемента массива:
cars[2] = "Mersedes"
print(cars)

#Возвращаем количество элементов:
x = len(cars)
print(x)

#Выводим каждый элемент в массиве:
for x in cars:
    print(x)
    
#Добавим в массив еще один элемент:
cars.append("Tesla")
print(cars)

#Удаляем второй элемент массива:
cars.pop(1)
print(cars)

#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list