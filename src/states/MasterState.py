from screens import *
from states import EScreenState


class MasterState:
    screen_state = EScreenState.Menu
    running = False
    window = None
    # Game Screen
    active_screen = None

    def __init__(self, window, running=True, screen_state=EScreenState.Menu):
        self.screen_state = EScreenState.Menu
        self.running = running
        self.screen_state = screen_state
        self.setActiveScreen(screen_state)
        self.window = window

    def setActiveScreen(self, es_state: EScreenState):
        switcher = {
            EScreenState.Menu: MenuScreen(self),
            EScreenState.Playing: PlayGameScreen(self),
            EScreenState.Minimax: MinimaxGameScreen(self)
        }
        self.screen_state = es_state
        self.active_screen = switcher.get(es_state, None)

    def getActiveScreen(self):
        return self.active_screen

    def isRunning(self):
        return self.running

    def getScreenState(self):
        return self.screen_state

    def actionChangeActiveScreen(self, es_state: EScreenState):
        self.setActiveScreen(es_state)
