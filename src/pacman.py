import pygame
from setting import Setting
from global_path import *
from states import EScreenState, GameState

GAME_SETTING = Setting()
os.environ['SDL_VIDEO_CENTERED'] = '1'


class PacmanGame():
    game_state = None

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(
            (GAME_SETTING.WIDTH, GAME_SETTING.HEIGHT))
        pygame.display.set_caption(GAME_SETTING.TITLE)
        pygame.display.set_icon(pygame.image.load(GAME_ICON))

        self.game_state = GameState(window=self.window, running=True, screen_state=EScreenState.Menu)
        self.clock = pygame.time.Clock()

    def run(self):
        while self.game_state.isRunning():
            # blit screen on window surface
            self.game_state.getActiveScreen().loop(self.window)

            pygame.display.update()
            
            self.clock.tick(60)


pacman_game = PacmanGame()
pacman_game.run()
pygame.quit()
