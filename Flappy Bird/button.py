import pygame
#This is as pygame sprite class
class Button():
    #button constructor
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        action = False
        #get mouse position
        mousePosition = pygame.mouse.get_pos()

        #check if mouse is over the button
        if self.rect.collidepoint(mousePosition):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        #draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
