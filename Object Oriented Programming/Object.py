#Parent Class
class Being:
    age=1
    weight=1

#Children Classes
class Jellyfish(Being):
    tentacles=25

class Cat(Being):
    paws=4

    def __init__(self,weight):
        self.weight=weight

class Person(Being):
    xPos=0.0
    yPos=0.0

    def communicate(self):
        self.weight=5

    def move(self):
        self.x+=1
        self.y+=1

#Code
personList=[Person(),Cat(5),Jellyfish()]
personList[0].age=2

for i in personList:
    print("Age: ", i.age)
    print("Weight: ",i.weight)