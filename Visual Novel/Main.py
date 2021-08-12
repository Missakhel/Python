import pygame, json
import pygame.freetype

def fileLoader(filename):
    file = open(filename,)
    data = json.load(file)
    return data

def textUpdate(font,data,screen):
    for index in range(1,5):
        font.render_to(screen, (25, 265+(index*16)), str(data["data"][index]["text"]), (255, 255, 255))

def main():
    pygame.init()
    screenSize = 900, 375
    font = pygame.freetype.SysFont("Unifont",14)
    black = 0,0,0
    screen = pygame.display.set_mode(screenSize)
    data = fileLoader("./TextFiles/0.json")
    #DATA[EXTERNAL DATA ARRAY] [INDEX] [KEY]
    image = pygame.image.load(str(data["data"][0]["image"]))
    initialized = True

    while initialized:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                initialized = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    data = fileLoader(str(data["data"][5]["file"]))
                    image = pygame.image.load(str(data["data"][0]["image"]))
                if event.key == pygame.K_RIGHT:
                    data = fileLoader(str(data["data"][6]["file"]))
                    image = pygame.image.load(str(data["data"][0]["image"]))
        background = image.get_rect()
        screen.fill(black)
        textUpdate(font, data, screen)
        screen.blit(image, background)
        pygame.display.flip()

if __name__ == "__main__":
    main()
