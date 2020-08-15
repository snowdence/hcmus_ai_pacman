from screens import *
from states import EScreenState
import importlib


class MasterState:
    screen_state = EScreenState.MENU
    running = False
    window = None
    # Game Screen
    active_screen = None

    def __init__(self, window, running=True, screen_state=EScreenState.MENU):
        self.screen_state = EScreenState.MENU
        self.running = running
        self.screen_state = screen_state
        self.setActiveScreen(screen_state)
        self.window = window

    def setActiveScreen(self, es_state: EScreenState):

        switcher = {
            EScreenState.MENU: 'MenuScreen',
            EScreenState.MINIMAX: 'MinimaxGameScreen',
            EScreenState.PLAYING: 'PlayGameScreen',
            EScreenState.LEVEL_1: 'FirstGameScreen',
            EScreenState.LEVEL_2: 'SecondGameScreen',
            EScreenState.LEVEL_3: 'ThirdGameScreen',
            EScreenState.LEVEL_4: 'FourthGameScreen'
        }

        class_name = switcher.get(es_state, None)
        module = importlib.import_module('screens')
        class_ = getattr(module, class_name)
        instance = class_(self)

        self.screen_state = es_state
        self.active_screen = instance

    def getActiveScreen(self):
        return self.active_screen

    def isRunning(self):
        return self.running

    def getScreenState(self):
        return self.screen_state

    def actionChangeActiveScreen(self, es_state: EScreenState):
        self.setActiveScreen(es_state)
