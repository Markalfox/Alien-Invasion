import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)

        self.ship = Ship(self.screen, self.settings)
        self.bullet = Bullet(self)

    def run_game(self):
        while True:
            self.__check_events()
            self.__update_screen()

            self.ship.update_position()
            self.bullet.check_bullet_position()

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.__check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.__check_keyup_events(event)

    def __check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.bullet.check_allowed_bullets(self)

    def __check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def __update_screen(self):
        self.screen.fill(self.settings.bg_color)

        self.ship.blit()

        self.bullet.fire_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
