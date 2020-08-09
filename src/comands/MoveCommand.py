from .Command import Command
from layers.entity import *


class MoveCommand(Command):
    unit: Layer = None
    state = None
    move_vector = (0, 0)

    def __init__(self, state, unit: Layer, move_vector):
        self.state = state
        self.unit = unit
        self.move_vector = move_vector

    def run(self):
        unit = self.unit
        x, y = unit.get_position()
        dx, dy = self.move_vector
        unit.set_position(x + dx, y + dy)
