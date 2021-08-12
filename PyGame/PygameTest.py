import sys, pygame, math
pygame.init()

size = screenWidth, screenHeight = 600, 600
speed = [0, 0]
black = 0, 0, 0
lastKey = 0

screen = pygame.display.set_mode(size)
slime = pygame.image.load("Vagyunk0.png")
slimeSprite = slime.get_rect()

# The "center" the sprite will orbit
center_x = (screenWidth - slimeSprite.width)/2
center_y = (screenHeight - slimeSprite.height)/2
angle = 0  # Current angle in radians
radius = (screenWidth - slimeSprite.width)/2    # How far away from the center to orbit, in pixels
quickness = .01  # How fast to orbit, in radians per frame

def resetStart(sprite, side):
    if (side == 0):
        sprite.y = 0 - sprite.height
        sprite.x = (screenWidth - sprite.width)/2
    elif (side == 1):
        sprite.y = (screenHeight - sprite.height)/2
        sprite.x = 0 - sprite.width
    elif (side == 2):
        sprite.y = (screenHeight - sprite.height)/2
        sprite.x = 0

def moveAround(sprite, speed):
    if (sprite.x == 0 and sprite.y == 0):
        speed =  [1,0]
    elif (sprite.x == screenWidth - sprite.width and sprite.y == 0):
        speed =  [0,1]
    elif (sprite.x == screenWidth - sprite.width and sprite.y == screenHeight - sprite.height):
        speed =  [-1,0]
    elif (sprite.x == 0 and sprite.y == screenHeight - sprite.height):
        speed =  [0,-1]
    return speed

def moveCross(sprite, side):
    if (sprite.y > screenHeight and side == True):
        resetStart(sprite, 1)
        side = False
    elif (sprite.x > screenWidth and side == False):
        resetStart(sprite, 0)
        side = True
    if (sprite.y < screenHeight + sprite.height and side == True):
        speed = [0, 1]
    elif (sprite.x < screenWidth + sprite.width and side == False):
        speed = [1, 0]
    return speed, side

while 1:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                resetStart(slimeSprite, 2)
                lastKey = 1
                speed = [0, -1]
            if event.key == pygame.K_UP:
                resetStart(slimeSprite, 2)
                lastKey = 2
            if event.key == pygame.K_RIGHT:
                resetStart(slimeSprite, 1)
                lastKey = 3
                side = False
    
    if (lastKey == 1):
        speed = moveAround(slimeSprite, speed)
    elif (lastKey == 2):
        slimeSprite.x = radius * math.sin(angle) + center_x
        slimeSprite.y = radius * math.cos(angle) + center_y
        angle += quickness
    elif (lastKey == 3):
        speed, side = moveCross(slimeSprite, side)

    slimeSprite = slimeSprite.move(speed)
    screen.fill(black)
    screen.blit(slime, slimeSprite)
    pygame.display.flip()
