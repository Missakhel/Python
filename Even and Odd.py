import random

def playerBet(totalPoints):
    while True:
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
    playerTurn = True
    computerOptions = ["odd", "even"]
    while (player > 0 and computer > 0):
        print("You have", player, "points and the computer has", computer, "points")
        bet = playerBet(player)
        computerBet = random.randint(1,computer)

        if playerTurn == True:
            answer = confirmating()
            playerTurn = False
        else:
            answer = computerOptions[random.randint(0,1)]
            playerTurn = True
            print("The computer thinks you wagered a",answer,"number of points")
        
        print("The computer wagered", computerBet, "points.")

        if ((answer == "E" and computerBet % 2 == 0) or 
            (answer == "even" and bet % 2 == 1) or 
            (answer == "O"  and computerBet % 2 == 1) or
            (answer == "odd" and bet % 2 == 0)):
            print("You win",computerBet,"points!")
            player += computerBet
            computer -= computerBet
        else:
            print("You lose",bet,"points...")
            player -= bet
            computer += bet
        print("-----")

    if player<=0:
        print("You've lost all your points... And you die.")
    else:
        print("The computer has lost all their points... You killed it!")

if __name__ == "__main__":
    main()
