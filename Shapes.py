counter = int(input("Ingresa el numero de segmentos: "))

# triangle
for i in range(1,counter+1):
    for t in range(1,i+1):
        print ("*",end="")
    print("")

print("")

#empty triangle
for a in range(1,counter+1):
    for g in range(1,a+1):
        if(a==counter):
            print("*", end="")
        else:
            if(g == 1):
                print("*", end="")
            elif(g == a):
                print("*", end="")
            else:
                print(" ", end="")
    print("")

print("")

#rectangle
for i in range(1, counter+1):
    for t in range(1, counter+1):
        print("*", end="")
    print("")

print("")

#empty rectangle
for i in range(1, counter+1):
    if(i==1):
        for t in range(1, counter+1):
            print("*", end="")
    elif(i==counter):
        for z in range(1, counter+1):
            print("*", end="")
    else:
        for y in range(1, counter+1):
            if(y==1):
                print("*", end="")
            elif(y==counter):
                print("*", end="")
            else:
                print(" ", end="")
    print("")
