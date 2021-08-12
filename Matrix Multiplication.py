def matrixBuilder(w,h):
    matrix = [[0 for x in range(h)] for y in range(w)]
    return matrix

def matrixAssigner(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix[x][y] = int(input(f"X{x+1}, Y{y+1} = "))
    return matrix

def matrixPrinter(matrix):
    for x in range(len(matrix)):
        print("|", end=" ")
        for y in range(len(matrix[0])):
            if (matrix[x][y]<10 and matrix[x][y]>-1):
                print("0", end="")
            print(f"{matrix[x][y]} |", end=" ")
        print("")

def matrixMultiplier(matrixA,matrixB,matrixR):
    for x in range(len(matrixR)):
        for y in range(len(matrixR[0])):
            addition = 0
            for r in range(len(matrixA[0])):
                addition += matrixA[x][r] * matrixB[r][y]
            matrixR[x][y] = addition
    return matrixR

def loopEnabler(option):
    while (option == "u"):
        option = input("\nDo you want to solve another multiplication? [y/n]: ").lower()
        if (option != "y" and option != "n"):
            option = "u"
            print("Please input a valid option!")
        elif (option == "n"):
            print("Program terminated.")
        return option

def main():
    loop = "y"
    while loop == "y":
        loop = "u"
        matrixA_x = int(input("Input matrix A width: "))
        matrixA_y = int(input("Input matrix A height: "))
        matrixB_x = int(input("Input matrix B width: "))
        matrixB_y = int(input("Input matrix B height: "))

        if (matrixA_x != matrixB_y):
            print("The matrix dimensions are incompatible, please input valid values")
            loop = loopEnabler(loop)
        else:
            matrixA = matrixBuilder(matrixA_y, matrixA_x)
            matrixB = matrixBuilder(matrixB_y, matrixB_x)
            matrixR = matrixBuilder(matrixA_y, matrixB_x)

            print("\nPlease assign values to the matrix A.")
            matrixA = matrixAssigner(matrixA)
            print("\nPlease assign values to the matrix B.")
            matrixB = matrixAssigner(matrixB)

            print("\nMatrix A:")
            matrixPrinter(matrixA)
            print("\nMatrix B:")
            matrixPrinter(matrixB)

            matrixR = matrixMultiplier(matrixA,matrixB,matrixR)
            print("\nResult Matrix:")
            matrixPrinter(matrixR)
            
            loop = loopEnabler(loop)

if __name__ == "__main__":
    main()
