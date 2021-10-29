import random

def playerBet(totalPoints):
    while True:
        print("You have", totalPoints, "points.")
        bet = int(input("How many points do you want to bet?: "))

        if bet > totalPoints:
            print("Please input a valid bet!")
        else:
            break
    return bet

def confirmating():
    while True:
        option = str(input("Did the computer bet an odd or even number of points? [O/E]: ")).upper()

        if option == "E" or option == "O":
            break
        elif option != "E" and option != "O":
            print("Please input a valid option")
    return option

def main():
    player = 10
    computer = 10
    
    while (player > 0 and computer > 0):
        bet = playerBet(player)
        computerBet = random.randint(1,computer)
        answer = confirmating()

        if (answer == "E" and computerBet%2 == 0 or answer == "O" and computerBet%2 == 1):
            print("The computer wagered", computerBet, "points.")
            print("You win",computerBet,"points!")
            player += computerBet
            computer -= computerBet
        else:
            print("The computer wagered", computerBet, "points.")
            print("You lose",bet,"points...")
            player -= bet
            computer += bet

    print("You've lost all your points... And you die.")

if __name__ == "__main__":
    main()
