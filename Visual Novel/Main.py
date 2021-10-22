import pygame, json
import pygame.freetype

def fileLoader(filename):
    file = open(filename,)
    data = json.load(file)
    return data

def textUpdate(font,data,screen):
    for index, item in enumerate (data["data"][1]["text"], start=0):
        font.render_to(screen, (25, 270+(index*16)), str(item), (255, 255, 255))
    for index, item in enumerate (data["data"][2]["options"], start=0):
        font.render_to(screen, (25, 280+((index+len(data["data"][2]["options"]))*16)), str(item["description"]), (255, 255, 255))

def main():
    pygame.init()
    screenSize = 900, 400
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
                    data = fileLoader(str(data["data"][2]["options"][0]["file"]))
                    image = pygame.image.load(str(data["data"][0]["image"]))

                if event.key == pygame.K_RIGHT and len(data["data"][2]["options"]) > 1:
                    data = fileLoader(str(data["data"][2]["options"][1]["file"]))
                    image = pygame.image.load(str(data["data"][0]["image"]))

                if event.key == pygame.K_UP and len(data["data"][2]["options"]) > 2:
                    data = fileLoader(str(data["data"][2]["options"][2]["file"]))
                    image = pygame.image.load(str(data["data"][0]["image"]))

                if event.key == pygame.K_DOWN and len(data["data"][2]["options"]) > 3:
                    data = fileLoader(str(data["data"][2]["options"][3]["file"]))
                    image = pygame.image.load(str(data["data"][0]["image"]))
        background = image.get_rect()
        screen.fill(black)
        textUpdate(font, data, screen)
        screen.blit(image, background)
        pygame.display.flip()

if __name__ == "__main__":
    main()
