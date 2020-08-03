import os
from os import path
from layers import *
from pygame.math import Vector2
from typing import List
import pygame
from setting import GAME_SETTING


class TileManager:

    ground_group:  List[Ground] = []
    player: List[Player] = None
    monster_group: List[Monster] = []
    coin_group = []
    wall_group = []

    def __init__(self):
        self.map_encode = []
        # list layer
        w, h = 40, 24
        # Matrix = [[0 for x in range(w)] for y in range(h)]
        self.map_tile: List[List[Layer]] = [
            [0 for x in range(w)] for y in range(h)]
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
                self.ground_group.append(Ground(self, Vector2(col, row)))
                # empty
                # self.map_tile[row][col] = Ground(self, Vector2(col, row))
                if ev == '1':
                    # wall
                    self.wall_group.append(Wall(self, Vector2(col, row)))
                elif ev == '2':
                    # food
                    self.coin_group.append(Coin(self, Vector2(col, row)))
                elif ev == '3':
                    # monster
                    self.monster_group.append(Monster(self, Vector2(col, row)))
                elif ev == 'P':
                    self.player = Player(self, Vector2(col, row))
        print("Parsed")

    def move_player(self, dx=0, dy=0):
        if(self.player.wall_collision(self.wall_group, dx, dy) is not True):
            self.player.set_position(
                self.player.position.x + dx, self.player.position.y + dy)

    def render(self, surface):

        for ground in self.ground_group:
            ground.render_tile(surface)

        for wall in self.wall_group:
            wall.render_tile(surface)

        for monster in self.monster_group:
            monster.render_tile(surface)

        for coin in self.coin_group:
            coin.render_tile(surface)

        self.player.render_tile(surface)


if __name__ == "__main__":
    pass
