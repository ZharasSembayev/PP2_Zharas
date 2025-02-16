#Now, we will create class of polymorphism:
class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive!")
class boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail")
class plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")
mycar = car("toyota", "camry")
myboat = boat("police",'president')
myplane = plane("Jet", "by1223")
for x in (mycar,myboat,myplane):
    x.move()