from bird import *
from pipe import *
from button import *
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()
fps = 60
screenWidth = 280
screenHeight = 500

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Flappy Bird by: los mas jotos')
font = pygame.font.SysFont('Arial', 60)
white = (255, 255, 255)

#game variables
groundScroll = 0
pipeFrequency = 1500 
scrollSpeed = 2
pipeGap = 150
lastPipe = pygame.time.get_ticks() - pipeFrequency
score = 0
passPipe = False

#aquí carga las imagenes de fondo, base y un boton en forma de pajaro
background = pygame.image.load('fondo.png')
buttonImage = pygame.image.load('boton.png')

def drawText(text, font, textCol, xPos, yPos):
    image = font.render(text, True, textCol)
    screen.blit(image, (xPos, yPos))

def resetGame():
    pipeGroup.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screenHeight / 2)
    score = 0
    return score
birdGroup = pygame.sprite.Group()
pipeGroup = pygame.sprite.Group()
#spawn bird in and add to group for collision detection
flappy = Bird(100, int(screenHeight / 2))
birdGroup.add(flappy)

#create restart button instance
button = Button(screenWidth // 2 - 50, screenHeight // 2 - 100, buttonImage)
run = True

#CYCLE BEGINS HERE
while run:
    clock.tick(fps)
    #draw background
    screen.blit(background, (0,0))
    birdGroup.draw(screen)
    birdGroup.update()
    pipeGroup.draw(screen)

    #check the score
    if len(pipeGroup) > 0:
        if birdGroup.sprites()[0].rect.left > pipeGroup.sprites()[0].rect.left\
            and birdGroup.sprites()[0].rect.right < pipeGroup.sprites()[0].rect.right\
            and passPipe == False:
            passPipe = True
        if passPipe == True:
            if birdGroup.sprites()[0].rect.left > pipeGroup.sprites()[0].rect.right:
                score += 1
                passPipe = False
    drawText(str(score), font, white, int(screenWidth / 2), 20)

    #collision detection
    if pygame.sprite.groupcollide(birdGroup, pipeGroup, False, False) or flappy.rect.top < 0:
        flappy.dead = True

    #esto sirve para las colisiones del pajaro con el piso
    if flappy.rect.bottom >= 500:
        flappy.dead = True
        flappy.flying = False

    if flappy.dead == False and flappy.flying == True:
        #la generacion de tubos
        currentTime = pygame.time.get_ticks()
        if currentTime - lastPipe > pipeFrequency:
            pipeHeight = random.randint(-100, 100)
            bottomPipe = Pipe(screenWidth, int(screenHeight / 2) + pipeHeight, -1, pipeGap)
            topPipe = Pipe(screenWidth, int(screenHeight / 2) + pipeHeight, 1, pipeGap)
            pipeGroup.add(bottomPipe)
            pipeGroup.add(topPipe)
            lastPipe = currentTime
        pipeGroup.update(scrollSpeed)

    #game over y se reinicia el juego
    if flappy.dead == True:
        if button.draw(screen) == True:
            flappy.dead = False
            score = resetGame()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flappy.flying == False and flappy.dead == False:
            flappy.flying = True

    pygame.display.update()

pygame.quit()
