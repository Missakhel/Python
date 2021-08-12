#Programa que grabe nombre, edad, curp y que diga si el usuario o el cliente ya está vacunado o no, permita agregar clientes, buscar cuantos están o no vacunados con funciones, porcentaje de vacunados y no vacunados
def dataInput(key):
    data = input(f"Please input {key}: ").upper()
    return {key:data}

def loopEnabler(option):
    while (option == "u"):
        option = input("\nDo you want input more data [y/n]: ").lower()
        if (option != "y" and option != "n"):
            option = "u"
            print("Please input a valid option!")
        elif (option == "n"):
            print("Program will be terminated.")
    return option

def dataClassification(array):
    percentageData = {"subjects": 0,"vaccinated": 0, "unvaccinated": 0, "unvalid data":0}
    for person in array:
        if person["is subject vaccinated? [Y/N]"] == "Y":
            percentageData["vaccinated"] += 1
        elif person["is subject vaccinated? [Y/N]"] == "N":
            percentageData["unvaccinated"] += 1
        else:
            percentageData["unvalid data"] += 1
        percentageData["subjects"]+=1
    percentage(percentageData)

def percentage(dataList):
    print("The total number of subjects is: ", dataList["subjects"])
    for key, value in dataList.items():
        print(f"Number and percentage of {key} is {value} |",(value * 100 / dataList["subjects"]),"%")

def main():
    print("VACCINATION REGISTRY & DATABASE (C)2021 VRDS")
    loop = "y"
    database = []
    dataArray = ["Name", "Age", "CURP", "is subject vaccinated? [Y/N]"]
    while loop == "y":
        loop = "u"
        subject = {}
        for i in dataArray:
            subject.update(dataInput(i))
        database.append(subject)
        loop = loopEnabler(loop)
    print("\nSUMMARY")
    for subject in database:
        print(subject)
    dataClassification(database)

if __name__ == "__main__":
    main()

#a = [
#    {
#        "whateverReturns":returnSomething(),
#        "age":25,
#        "name":"A Guy",
#        "vaccines":["Measles","COVID"],
#        "parents":[{
#            "name":"Mom"
#        }]
#    },
#    {"age":18,"name":"Guy 2"}
#]
#print(a)
