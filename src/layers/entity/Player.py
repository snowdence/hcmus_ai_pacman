from .Layer import Layer

import math
from pygame.math import Vector2

from gpath import *


class Player(Layer):
    def __init__(self, tile_manager, position, cell_size=None):
        super().__init__(position=position, cell_size=cell_size,
                         image_file=PATH_IMAGE + "pacman.png")
        self.tile_manager = tile_manager

    def render(self, surface):
        self.render_tile(surface)

    def wall_collision(self, wall_group, dx=0, dy=0):
        for wall in wall_group:
            if (self.check_collision(wall, dx, dy)):
                return True
        return False

    def eat_coin(self, coin_group):
        for coin in coin_group:
            if(self.check_collision(coin, 0, 0)):
                coin.hide()

    def mahattan_distance(self, ghost):
        gx, gy = ghost.position.x, ghost.position.y
        x, y = self.position.x, self.position.y
        dis = abs(x-gx) + abs(y - gy)
        return dis

    def ghost_mahattan_check_danger(self, ghost_group):
        for ghost in ghost_group:
            mad = self.mahattan_distance(ghost)
            if mad > 3:
                return True
