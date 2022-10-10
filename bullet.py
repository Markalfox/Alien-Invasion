import pygame


class Bullet:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        self.rect = pygame.Rect(ai_game.ship.image_rect.midtop, ai_game.settings.bullet_size)
        self.y = float(self.rect.y)

    def update_position(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
