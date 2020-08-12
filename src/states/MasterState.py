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
        """Set state screen

        Args:
            es_state (EScreenState): Enum value of state screen
        """

        switcher = {
            EScreenState.Menu: MenuScreen(self),
            EScreenState.Playing: PlayGameScreen(self),
            EScreenState.Minimax: MinimaxGameScreen(self)
        }
        self.screen_state = es_state
        self.active_screen = switcher.get(es_state, None)

    def getActiveScreen(self):
        """[Get current active state screen]

        Returns:
            [EScreenState]: [Current state]
        """
        return self.active_screen

    def isRunning(self):
        """[Check game is running. Whole game, not a level]

        Returns:
            [type]: [description]
        """
        return self.running

    def getScreenState(self):
        """[Get current screen]

        Returns:
            [GameScreen]: [Current game screen]
        """
        return self.screen_state

    def actionChangeActiveScreen(self, es_state: EScreenState):
        """Change active screen

        Args:
            es_state (EScreenState): [description]
        """
        self.setActiveScreen(es_state)
