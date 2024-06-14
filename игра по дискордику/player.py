import pygame

class Player():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('img/player/player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
    def update_screen(self):
        pass