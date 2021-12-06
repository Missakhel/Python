import pygame
#This is as pygame sprite class
class Pipe(pygame.sprite.Sprite):
    #pipe constructor
    def __init__(self, xPos, yPos, position, pipeGap):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pipe.png')
        self.rect = self.image.get_rect()
        #position 1 is from the top, -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [xPos, yPos - int(pipeGap / 2)]
        if position == -1:
            self.rect.topleft = [xPos, yPos + int(pipeGap / 2)]

    def update(self, scrollSpeed):
        self.rect.x -= scrollSpeed
        if self.rect.right < 0:
            self.kill()
