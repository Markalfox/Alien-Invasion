import pygame


class Ship:

    def __init__(self, ai_game_screen):
        self.ai_game_screen = ai_game_screen
        self.ai_game_screen_rect = ai_game_screen.get_rect()

        self.image = pygame.image.load('images/alien_ship.png')
        self.image_rect = self.image.get_rect()
        self.image_rect.midbottom = self.ai_game_screen_rect.midbottom

    def blit(self):
        self.ai_game_screen.blit(self.image, self.image_rect)
