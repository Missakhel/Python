#Animal class definition
class Animal:
    #Properties
    name = "Hybrid"
    species = ""
    family = ""

    #Methods
    def eat(self, food):
        print(f"{self.name} says: Yum, {food}")

#Object instance creation
animalObj = Animal()
animalTest = Animal()

#Using object instances
animalTest.name = "Chimaera"
print(animalObj.name)
animalObj.eat("cheese")
animalTest.eat("meat")