import random

def isColumnRepeated(matrix, column, value):
    for row in matrix:
        if row[column] == value:
            return True
        return False

def getMatrix():
    matrix=[]
    for row in range(9):
        columns = []
        randomRow = random.randint(3,4)
        for columns in range(9):
            columnValue = random.randint(0,9)
            if columnValue in columns or randomRow==0 or isColumnRepeated(matrix,columns,columnValue):
                columnValue=0
            else:
                randomRow-=1
            columns.append(columnValue)
        matrix.append(columns)

def main():
    matrix = [
        [3,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9]
    ]

    print(matrix)
    row = int(input("Which row? "))
    column = int(input("Which column? "))
    number = int(input("Which number? "))

    for i in matrix[row]:
        if matrix[i] == number:
            print("You can't put that number here")
        else:
            matrix[row]=number
    for matrix[row] in matrix:
        if matrix[row] == number:
            print("You can't put that number here")
        else:
            matrix[row] = number

main()
