import pygame
from setting import Setting
from gpath import *
from states import EScreenState, MasterState

GAME_SETTING = Setting()
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.mixer.init()
sound = pygame.mixer.Sound(PATH_ASSETS + "sound/super_mario.wav")


class PacmanGame():
    master_state = None

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(
            (GAME_SETTING.WIDTH, GAME_SETTING.HEIGHT))
        pygame.display.set_caption(GAME_SETTING.TITLE)
        pygame.display.set_icon(pygame.image.load(GAME_ICON))
        self.master_state = MasterState(
            window=self.window, running=True, screen_state=EScreenState.LEVEL_1)
        self.clock = pygame.time.Clock()
        sound.play()

    def run(self):
        while self.master_state.isRunning():
            # blit screen on window surface
            self.master_state.getActiveScreen().loop(self.window)

            pygame.display.update()

            self.clock.tick(60)


pacman_game = PacmanGame()
pacman_game.run()
pygame.quit()
