import os
from os import path
from layers import *
from pygame.math import Vector2
from typing import List
import pygame


class TileManager:
    def __init__(self):
        self.map_encode = []
        # list layer
        w, h = 40, 24
        # Matrix = [[0 for x in range(w)] for y in range(h)]
        self.map_tile: List[List[Layer]] = [[0 for x in range(w)] for y in range(h)]
        self.player = None
        self.load_map()
        self.parse_map()

    def load_map(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)
        for row, tiles in enumerate(self.map_data, start=0):
            row_p = []
            for col, tile in enumerate(tiles, start=0):
                if tile in ['.', '1', '2', '3', 'P']:
                    row_p.append(tile)
            self.map_encode.append(row_p.copy())
        print("load ok")

    def parse_map(self):
        for (row, rv) in enumerate(self.map_encode, start=0):
            for (col, rc) in enumerate(self.map_encode[row], start=0):
                ev = self.map_encode[row][col]
                if ev == '.':
                    # empty
                    self.map_tile[row][col] = Ground(self, Vector2(row, col))
                elif ev == '1':
                    # wall
                    self.map_tile[row][col] = Wall(self, Vector2(row, col))
                elif ev == '2':
                    # food
                    self.map_tile[row][col] = Coin(self, Vector2(row, col))
                elif ev == '3':
                    # monster
                    self.map_tile[row][col] = Monster(self, Vector2(row, col))
                elif ev == 'P':
                    self.player = Player(self, Vector2(row, col))
                    self.map_tile[row][col] = self.player
        print("Parsed")

    def move_player(self, dx=0, dy=0):
        self.player.set_position(self.player.position.x + dx * 32, self.player.position.y + dy * 32)

    def render(self, surface):
        for (row, _) in enumerate(self.map_tile, start=0):
            for (col, _) in enumerate(self.map_tile[row], start=0):
                # print("Row {}, col {}".format(row, col))
                self.map_tile[row][col].render_tile(surface)
        self.player.render_tile(surface)


if __name__ == "__main__":
    pass
