while True:
    size = int(input("Please input a size value for the matrix: "))
    if (size % 2 != 0):
        matrix = [[False]*size]*size
        break
    else:
        print("The input value is invalid.")

for Xindex, array in enumerate(matrix):
    for Yindex, value in enumerate(array):
        if (Xindex == Yindex):
            value = True
        print(f"{int(value)}", end=" ")
    print("\n")

print("-"*10)
matrix = [[False]*size]*size

for Xindex, array in enumerate(matrix):
    for Yindex, value in enumerate(array):
        if (Xindex == size//2 or Yindex == size//2):
            value = True
        print(f"{int(value)}", end=" ")
    print("\n")

print("-"*10)
matrix = [[False]*size]*size

for Xindex, array in enumerate(matrix):
    for Yindex, value in enumerate(array):
        if (Xindex == Yindex or Yindex == size-Xindex-1):
            value = True
        print(f"{int(value)}", end=" ")
    print("\n")