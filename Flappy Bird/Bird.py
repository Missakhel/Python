import pygame
#This is as pygame sprite class which has built-in update and draw functions
#No need to blit
class Bird(pygame.sprite.Sprite):
    flying = False
    dead = False
    #constructor del pajaro
    def __init__(self, xPos, yPos):
        #initializing sprite
        pygame.sprite.Sprite.__init__(self)
        self.baseImage = pygame.image.load('bird.png')
        self.image = self.baseImage
        self.rect = self.baseImage.get_rect()
        self.rect.center = [xPos, yPos]
        self.velocity = 0
        self.clicked = False

    def update(self):
        if self.flying == True:
            #gravedad
            self.velocity += 0.5
            #limites de la gravedad para que no siga acelerando
            if self.velocity > 8:
                self.velocity = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.velocity)

        if self.dead == False:
            #salto
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.velocity = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        
                #rotación del pajaro
            self.image = pygame.transform.rotate(self.baseImage, self.velocity * -2)
