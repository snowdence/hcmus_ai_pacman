from .state import State


class Expandable:
    cost: int = 0
    state = None
    actionSequence = []  # list child actions

    def __init__(self):
        self.state = State()
        self.actionSequence = []
        self.cost = 0

    def setCost(self, val):
        self.cost = val

    def getCost(self):
        return self.cost
