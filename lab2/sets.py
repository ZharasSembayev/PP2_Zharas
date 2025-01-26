thisset = {"apple", "banana", "cherry", "Kz", True , 1 , 2}
print(thisset)
#Duplicate values will be ignored:
#True and 1 is considered the same value:

myset = {"apple", "banana", "cherry"}
print(type(myset))

#ACCESS Sets:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
#Add Set:
a = {"Almaty", "Kazakh", "Arman", "Russian"}
a.add("English")
print(a)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Remove Set:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
thisset.remove("apple")

#LOOP Sets:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#JOIN Sets:
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

#METHODS Sets:

"""
add()	 	Adds an element to the set
clear()	 	 Removes all the elements from the set
copy()	 	 Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
    
"""
