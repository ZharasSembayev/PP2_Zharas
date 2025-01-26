#LISTS:
thislist = ["apple", "banana", "cherry"]
print(thislist)
a = ["Zharas" , "Asan" , "Amina"]
print(len(a))
print(type(a))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

kz = list(("Ufc", "Rebook"))
print(kz)

#Access Lists:
a = ["apple", "banana", "cherry", "kazakh"]
print(a[1])
print(a[-1])
print(a[2:])
print(a[:1])
print(a[1:3])

#Change List Items:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Add List:
a = ["apple", "banana", "cherry"]
a.append("orange")
print(a)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove List:

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
thislist.clear()
print(thislist)

#LOOP Lists:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
#List Comprehension:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#Sort Lists:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)

#COPY Lists:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#JOIN Lists:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#METHODS:
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#Index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list



