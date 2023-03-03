import pygame
from pygame.sprite import Sprite

class Gun(Sprite):

    def __init__(self, screen):
        # initilaization gun(ship)
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        # drawing gun(ship)
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        # update position for gun
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        elif self.mleft and self.rect.left > self.screen_rect.left:
            self.center -= 1.5

        self.rect.centerx = self.center


    def create_gun(self):
        #create gun on center upside
        self.center = self.screen_rect.centerx