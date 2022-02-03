import random

secretArray = ["secret","classified","unrevealed","undisclosed","unknown","restricted","unofficial","unnoticeable","shrouded","clandestine"]
wordArray = []
clueArray = []
playing = True
setting = True
word = ""
secretWord = secretArray[random.randint(0,len(secretArray)-1)]
tries = 1
specialCharacter = "#"

for letter in secretWord:
    wordArray.append("_")

while setting:
    difficulty = int(input("Please input a difficulty level (0,1,2): "))
    if(difficulty>2):
        print("Please input a valid option")
    else:
        print(f"Enter '#' if you need to uncover clues!")
        tries += (10*(2-difficulty))
        for index in range (2-difficulty):
            wordArray[random.randint(0,len(secretWord)-1)] = "#"
        setting = False

while playing:
    if word != secretWord and tries > 0:
        for char in wordArray:
            print (f" {char}", end=" ")
        print(f"\n You've got {tries} tries left!")
        word = input(" Please input a word to guess the secret word: ")
        if word == specialCharacter:
            for index, character in enumerate(wordArray):
                if character == specialCharacter:
                    wordArray[index] = secretWord[index]
        elif len(word)!=len(secretWord):
            print("Your word must be the same size as the secret word!")
        else:
            for index, letter in enumerate(word):
                if(letter == secretWord[index]):
                    wordArray[index] = letter
            tries -= 1
    elif tries == 0:
        print("You Lost! the secret word was:", secretWord)
        playing = False
    else:
        print("Congratulations! You've guessed the secret word:", secretWord)
        playing = False