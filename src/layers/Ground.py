from .Layer import Layer

import math
from pygame.math import Vector2

from global_path import *


class Ground(Layer):
    def __init__(self, tile_manager, position, cell_size=None):
        super().__init__(position=position, cell_size=cell_size, image_file=PATH_IMAGE + "land_5.png")
        self.tile_manager = tile_manager

    def render(self, surface):
        self.render_tile(surface)
