#numeros = [4, 5, 6, 7]
#numeros2 = [4, 6, 9]

#def identificador(numeroparabuscar, matriz):
#    for elem in matriz:
#        if numeroparabuscar == elem:
#            return True
#    return False

#x = int(input("Introduce el numero a buscar: "))
#print(identificador(x, numeros))
#print(identificador(x, numeros2))

inventory = []
loop = "y"

#FUNCTION TO VERIFY IF INPUT IS IN THE INVENTORY
def compare(inventory, item):
    if item in inventory:
        return True
    else:
        return False

#FUNCTION TO CONVERT INPUTS TO LOWERCASE
def lower(string):
    string = string.lower()
    return string

#FUNCTION TO DETERMINE WHETHER TO ADD ITEM TO INVENTORY
def management(inventory):
    item = str(input("Please input the item you want to add: "))
    item = lower(item)

    if (compare(inventory, item)) == True:
        print("Sorry, that item is already in your inventory.")

    else:
        inventory.append(item)
    return inventory

while loop == "y":
    loop = str(input("Do you wish to add an item to your inventory? [y/n]: "))
    loop = lower(loop)

    if(loop=="y"):
        inventory = management(inventory)
        print("Items on your inventory: ", inventory)

    elif (loop=="n"):
        break

    else:
        print("Unrecognized input, please try again.")
        loop = ("y")