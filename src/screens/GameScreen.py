from screens import EventScreen
from states import GameState
import pygame


class GameScreen(EventScreen):
    state: GameState = None

    def __init__(self, state):
        EventScreen.__init__(self)
        self.state = state
        print("init state", self.state.isRunning())
        print("Init game screen")

    def loop(self, window):
        self.process_input()
        self.update()
        self.render(window)

        self.clean()

    def on_exit(self):
        self.state.running = False

    def process_input(self):
        for event in pygame.event.get():
            self.on_event(event)

    def update(self):
        pass

    def render(self, window):
        pass

    def clean(self):
        pass
