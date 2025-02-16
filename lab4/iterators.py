mytuple = ("Men", "Sen", "Ol")
m = iter(mytuple)

print(next(m))
print(next(m))
print(next(m))

mystr = "Pinapple"
m = iter(mystr)
print(next(m))

#We will create Iterator:
class It:
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
myit = It()
m = iter(myit)
for x in m:
    print(x) 
