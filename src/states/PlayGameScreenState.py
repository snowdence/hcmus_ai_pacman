from layers.entity import *
import pygame
from typing import List
from setting import *


class PlayGameScreenState:
    players = None
    wall_layer = []  # full to detect collision
    ground_layer = []  # full to render
    monster_layer = []  # unit
    coin_layer = []  # unit

    entities = dict()  # keep all entities

    map_encode = []  # 0 1 2 3 P map

    def __init__(self):
        self.ground_layer = [[None] * (GAME_SETTING.WIDTH // 32)] * (GAME_SETTING.HEIGHT // 32)
        self.wall_layer = [[None] * (GAME_SETTING.WIDTH // 32)] * (GAME_SETTING.HEIGHT // 32)

        self.entities = {
            'ground': self.ground_layer,
            'wall': self.wall_layer,
            'monster': self.monster_layer,
            'coin': self.coin_layer
        }

        print("init state play game")

    def add_player(self, player: Player):
        self.players = player

    def add_wall(self, wall_layer: List[Wall]):
        self.wall_layer = wall_layer.copy()

    def add_monster(self, monster_layer: List[Monster]):
        self.monster_layer = monster_layer.copy()

    def add_coin(self, coin_layer: List[Coin]):
        self.coin_layer = coin_layer.copy()

    def action_render_all(self, window):
        for layer, layer_val in self.entities.items():
            for entity in layer_val:
                entity.render_tile(window)

        self.players.render_tile(window)

    def action_solve(self, level=1, map_name='map_lv1.txt', algorithm='bfs'):
        pass

    def minimax_solve(self):

        pass


if __name__ == '__main__':
    a = PlayGameScreenState()
