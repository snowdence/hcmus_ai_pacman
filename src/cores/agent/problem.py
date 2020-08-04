from .state import State
from .action import Action


class Problem:
    def __init__(self):
        pass

    def result(self, s: State, a: Action):
        pass

    def actions(self, s: State):
        pass

    def goalTest(self, s: State):
        pass
