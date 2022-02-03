class Person:
    name = ""
    age = 0
    sex = ""
    location = ""

    def __init__(self, name, age, sex, location):
        self.name = name
        self.age = age
        self.sex = sex
        self.location = location

def printData(nameArray):
    print("-"*5)
    for index, person in enumerate(nameArray):
        print("Person", index+1)
        print("Name: ", person.name)
        print("Age: ", person.age)
        print("Sex: ", person.sex)
        print("Location: ", person.location)
        print("-"*5)

def main():
    insertingNames = True
    name = ""
    age = 0
    sex = ""
    location = ""
    nameArray = []
    loop = ""
    counter = 0

    unaccepted = True
    sumNumber = 0
    indexNumber = 0
    
    while insertingNames:
        name = str(input("Please input the name: "))
        age = int(input("Please input the age: "))
        sex = str(input("Please input the sex: "))
        location = str(input("Please input the location: "))

        person = Person(name, age, sex, location)
        nameArray.append(person)
        counter += 1

        if counter>1:
            loop = str(input("If you want to exit the input phase, press 'y': "))
            if loop.lower() == "y":
                insertingNames = False

    printData(nameArray)

    sumNumber = int(input("Insert a number to sum to age: "))
    while unaccepted:
        indexNumber = int(input("Insert the index number to modify: "))

        if(indexNumber > len(nameArray)-1 or indexNumber < 0):
            print("The index number is unacceptable, please input a valid number. ")
        else:
            unaccepted = False

    for indexMod in range(0,len(nameArray)):
        if indexMod % indexNumber == 0:
            nameArray[indexMod].age += sumNumber
    
    print("Modified Data:")
    printData(nameArray)

if __name__ == "__main__":
    main()

