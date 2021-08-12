import pygame, sys
from Tamagotchi import Tamagotchi
from MovementManager import MovementManager

def main():
    pygame.init()
    screenSize = screenWidth, screenHeight = 600, 600
    black = 0,0,0
    screen = pygame.display.set_mode(screenSize)
    vagyunk = Tamagotchi()
    movementManager = MovementManager()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressedKey = pygame.key.get_pressed()
        if pressedKey[pygame.K_UP] or pressedKey[pygame.K_w]:
            movementManager.Move(vagyunk.rectArray[vagyunk.emotion],"up",0)
        if pressedKey[pygame.K_DOWN] or pressedKey[pygame.K_s]:
            movementManager.Move(vagyunk.rectArray[vagyunk.emotion],"down",screenHeight)
        if pressedKey[pygame.K_LEFT] or pressedKey[pygame.K_a]:
            movementManager.Move(vagyunk.rectArray[vagyunk.emotion],"left",0)
        if pressedKey[pygame.K_RIGHT] or pressedKey[pygame.K_d]:
            movementManager.Move(vagyunk.rectArray[vagyunk.emotion],"right",screenWidth)

        #print(f"Your pet is {vagyunk.stateList[vagyunk.emotion]}")
        #print("AVAILABLE ACTIONS")
        #for key, value in vagyunk.actionDict.items():
        #    print(f"[{value}] {key}")
        #action = int(input("PLEASE INPUT A NUMBER TO DO THE FOLLOWING ACTIONS: ")) - 1
        #vagyunk.emotion = vagyunk.stateMatrix[action][vagyunk.emotion]

        if vagyunk.emotion == 10:
            print("YOUR PET IS DEAD.")

        screen.fill(black)
        screen.blit(vagyunk.spriteArray[vagyunk.emotion],
                    vagyunk.rectArray[vagyunk.emotion])
        pygame.display.flip()

if __name__ == "__main__":
    main()
