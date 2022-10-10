import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.ship = Ship(self.screen)

    def run_game(self):
        while True:
            self.__check_events()
            self.__update_screen()

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def __update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blit()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
