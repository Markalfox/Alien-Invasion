import pygame


class Bullet:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        self.rect = pygame.Rect(ai_game.ship.image_rect.midtop, ai_game.settings.bullet_size)
        self.y = float(self.rect.y)

        self.bullets = []

    def update_position(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def fire_bullet(self):
        for bullet in self.bullets:
            bullet.draw_bullet()
            bullet.update_position()

    def check_bullet_position(self):
        for bullet in self.bullets:
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def check_allowed_bullets(self, ai_game):
        if len(self.bullets) < self.settings.bullet_allowed:
            self.bullets.append(Bullet(ai_game))
