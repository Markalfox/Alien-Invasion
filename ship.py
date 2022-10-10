import pygame


class Ship:

    def __init__(self, ai_game_screen, settings):
        self.settings = settings

        self.ai_game_screen = ai_game_screen
        self.ai_game_screen_rect = ai_game_screen.get_rect()

        self.image = pygame.image.load('images/alien_ship.png')
        self.image_rect = self.image.get_rect()
        self.image_rect.midbottom = self.ai_game_screen_rect.midbottom

        self.x = float(self.image_rect.x)

        self.moving_right = False
        self.moving_left = False

    def blit(self):
        self.ai_game_screen.blit(self.image, self.image_rect)

    def update_position(self):
        if self.moving_right and (self.image_rect.right < self.ai_game_screen_rect.right):
            self.x += self.settings.ship_speed

        if self.moving_left and (self.image_rect.left > self.ai_game_screen_rect.left):
            self.x -= self.settings.ship_speed

        self.image_rect.x = self.x
