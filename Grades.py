def average(summation, loop):
    return (summation/loop)

def confirmating(value):
    while True:
        if value == 0:
            confirmation = str(input("Do you want to input another grade? [Y/N]: ")).upper()
        elif value == 1:
            confirmation = str(input("Do you want to make another calculation? [Y/N]: ")).upper()

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
        grading = True
        summation = 0
        loop = 0
        while grading:
            summation += float(input("Please input a grade: "))
            loop += 1
            grading = confirmating(0)
        print ("The average grade is:",average(summation, loop))
        run = confirmating(1)

if __name__ == "__main__":
    main()
