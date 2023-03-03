import pygame

class Ino(pygame.sprite.Sprite):
    #class for one enemy
    def __init__(self,screen):
        #init for enemy and stand for first position enemy
        super(Ino,self,).__init__()
        self.screen=screen
        self.image=pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def draw(self):
        #drawing enemy
        self.screen.blit(self.image,self.rect)


    def update(self):
        #aliens go to the ship
        self.y +=0.1
        self.rect.y = self.y