import os
import pygame
from setting import Setting
from global_path import *

from screens import MenuScreen

GAME_SETTING = Setting()
os.environ['SDL_VIDEO_CENTERED'] = '1'


class PacmanGame():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(
            (GAME_SETTING.WIDTH, GAME_SETTING.HEIGHT))
        pygame.display.set_caption(GAME_SETTING.TITLE)
        pygame.display.set_icon(pygame.image.load(GAME_ICON))

        self.clock = pygame.time.Clock()
        self.running = True

        # Modes
        self.playGameMode = None
        self.overlayGameMode = MenuScreen()
        self.currentActiveMode = 'Overlay'

    def update(self):
        pass

    def run(self):
        while self.running:
            if self.currentActiveMode == 'Overlay':
                self.overlayGameMode.process_input()
                self.overlayGameMode.update()
            if self.playGameMode is not None:
                self.playGameMode.render(self.window)
            else:
                self.window.fill((0, 0, 0))
            if self.currentActiveMode == 'Overlay':
                darkSurface = pygame.Surface(
                    self.window.get_size(), flags=pygame.SRCALPHA)
                pygame.draw.rect(darkSurface, (0, 0, 0, 150),
                                 darkSurface.get_rect())
                self.window.blit(darkSurface, (0, 0))
                self.overlayGameMode.render(self.window)

            pygame.display.update()
            self.clock.tick(60)


pacman_game = PacmanGame()
pacman_game.run()
pygame.quit()
