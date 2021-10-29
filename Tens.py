#Un programa donde el usuario pueda ingresar números del 1 al 50. No mayores, no menores. E imprimir los primeros 3 números por cada decena
#Ej, el usuario ingresó 1, 2, 3, 4, 13, 14, 15, 16
def confirmating(value):
    while True:
        if value == 0:
            confirmation = str(input("Do you want to input another number? [Y/N]: ")).upper()
        elif value == 1:
            confirmation = str(input("Do you want to continue? [Y/N]: ")).upper()

        if confirmation == "N":
            answer = False
            break
        elif confirmation == "Y":
            answer = True
            break
        elif confirmation != "Y" and confirmation != "N":
            print("Please input a valid option")
    return answer

def main():
    run = True
    while run:
        listing = True
        numberList = []
        numberMatrix = [[], [], [], [], []]

        while listing:
            number = int(input("Please input a number between 1 and 50: "))
            if (number >= 0 and number < 50):
                numberList.append(number)
                listing = confirmating(0)
            else:
                print("Make sure the number is greater than 1 and lower than 50!")

        for number in numberList:
            for iteration in range(5):
                if (number > iteration*10 and number<(iteration+1)*10):
                    numberMatrix[iteration].append(number)

        for count, array in enumerate(numberMatrix):
            if (len(array)>0):
                print("Group of", count*10, "s:")
                if (len(array) > 3):
                    print("[", end="")
                    for index in range(3):
                        print(array[index], end=",")
                    print("]")
                else:
                    print(array)
        run = confirmating(1)

if __name__ == "__main__":
    main()
