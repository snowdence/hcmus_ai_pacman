import os
from os import path
from layers.entity import *
from pygame.math import Vector2
from typing import List
import pygame
from setting import GAME_SETTING
from cores.search.bfs import *

from gpath import *

from cores.minimax.GameState import GameState
from cores.minimax.GameStateData import GameStateData
from cores.minimax.MiniMaxAgent import MiniMaxAgent, AlphaBetaAgent
from cores.minimax.layout import *
from cores.minimax.GhostAgents import GhostAgent, DirectionalGhost


class ThirdLevelManager:
    ground_group: List[Ground] = []
    player: Player = None
    monster_group: List[Monster] = []
    coin_group = []
    wall_group = []
    result_action_code = []
    started = False

    # game state
    game = None

    def __init__(self, game):
        self.map_encode = []
        # list layer
        #w, h = 10, 10
        # Matrix = [[0 for x in range(w)] for y in range(h)]
        # self.map_tile: List[List[Layer]] = [
        #    [0 for x in range(w)] for y in range(h)]
        self.player = None
        self.load_map('mini.txt')
        self.parse_map()

        self.step = 0
        self.titleFont = pygame.font.Font(
            PATH_ASSETS + "font/BD_Cartoon_Shout.ttf", 72)
        self.itemFont = pygame.font.Font(
            PATH_ASSETS + "font/BD_Cartoon_Shout.ttf", 48)

        self.game = game
        self.initial_ghost_indexes = game.state.get_ghost_position()

    def load_map(self, file_map='map.txt'):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, PATH_MAP + file_map), 'rt') as f:
            for line in f:
                self.map_data.append(line)
        for row, tiles in enumerate(self.map_data, start=0):
            row_p = []
            for col, tile in enumerate(tiles, start=0):
                if tile in ['.', '1', '2', '3', 'P']:
                    row_p.append(tile)
            self.map_encode.append(row_p.copy())
        print("load map {} successfully!!!".format(file_map))

    def parse_map(self):
        for row, rv in enumerate(self.map_encode, start=0):
            for col, rc in enumerate(self.map_encode[row], start=0):
                ev = self.map_encode[row][col]
                self.ground_group.append(Ground(self, Vector2(col, row)))
                # empty
                # self.map_tile[row][col] = Ground(self, Vector2(col, row))
                if ev == '1':
                    # wall
                    self.wall_group.append(Wall(self, Vector2(col, row)))
                elif ev == '.':
                    # food
                    self.coin_group.append(Coin(self, Vector2(col, row)))
                elif ev == '3':
                    # monster
                    self.monster_group.append(Monster(self, Vector2(col, row)))
                elif ev == 'P':
                    self.player = Player(self, Vector2(col, row))
        print("Parsed")

    def run(self):
        game = self.game
        game.num_moves = 0
        agent_index = game.start_index
        num_agents = len(game.agents)
        while not game.game_over:

            agent = game.agents[agent_index]

            action = None

            observation = game.state.deepcopy()

            action = agent.get_action(observation)
            game.move_history.append((agent_index, action))
            game.state = game.state.generate_successor(agent_index, action)
            game.rules.process(game.state, self)
            print("Agent {0} action: {1}".format(agent_index, action))
            print("Epoch agent {0}, Num moves{1}".format(
                agent_index, game.num_moves))

            if agent_index == num_agents - 1:
                game.num_moves += 1
                print("Score :", game.state.data.score)
                print("Food :", game.state.get_num_food())
                print(game.state.get_pacman_position())
                print(game.state.get_ghost_position())

            if agent_index == num_agents - 1:
                agent_index = 0
            else:
                agent_index += 1

            # display update
        print("End ")

    def move_player(self, dx=0, dy=0):
        if (self.player.wall_collision(self.wall_group, dx, dy) is not True):
            self.player.set_position(
                self.player.position.x + dx, self.player.position.y + dy)
    def monster_can_move(self, index, pos):
        if index > 0:
            ix, iy = self.initial_ghost_indexes[index-1]
            x, y = pos
            return abs(ix-x) <= 1 and abs(iy-y) <= 1
        return False
    def update(self):
        game = self.game
        num_agents = len(game.agents)
        if game.game_over:
            print("End")
            return
        for agent_index in range(num_agents):
            agent = game.agents[agent_index]

            action = None
            observation = game.state.deepcopy()
            if agent_index == 0:
                observation.optimize_mahattan_danger()

            action = agent.get_action(observation)
            game.move_history.append((agent_index, action))
            temp_state = game.state.generate_successor(agent_index, action)
            if self.monster_can_move(agent_index, temp_state.get_ghost_pos(agent_index)) or agent_index == 0:
                game.state = game.state.generate_successor(agent_index, action)
                game.rules.process(game.state, self)
                print("Agent {0} action: {1}".format(agent_index, action))
                print("Epoch agent {0}, Num moves{1}".format(
                    agent_index, game.num_moves))

                if agent_index == 0:
                    self.move_pacman(game.state.get_pacman_position())
                elif agent_index > 0:
                    self.move_monster(game.state.get_ghost_state(
                        agent_index).getPosition())

                if agent_index == num_agents - 1:
                    game.num_moves += 1
                    print("Score :", game.state.data.score)
                    print("Food :", game.state.get_num_food())
                    print(game.state.get_pacman_position())
                    print(game.state.get_ghost_position())
                    if game.state.collide_ghosts_pos(game.state.get_pacman_position()) == True:
                        game.game_over = True
                        print("Chet roi!!!!")
                if game.game_over:
                    # pygame.display.set_mode((GAME_SETTING.M_WIDTH, GAME_SETTING.M_HEIGHT))
                    # pygame.display.set_caption(GAME_SETTING.TITLE)
                    # pygame.display.set_icon(pygame.image.load(GAME_ICON))

                    # game_over = self.titleFont.render(
                    #     "GAME OVER", True, (100, 0, 0))
                    # surface.blit(game_over, (70, 170))

                    # score = self.itemFont.render("Score: " + str(self.step), True, (100, 0, 0))
                    # surface.blit(score, (200, 275))

                    print("End")
                    return

                if agent_index == num_agents - 1:
                    agent_index = 0

                else:
                    agent_index += 1

    def move_pacman(self, new_position):
        x, y = new_position
        self.player.set_position(x, y)
        self.player.eat_coin(self.coin_group)

    def move_monster(self, new_position):
        x, y = new_position

        for monster in self.monster_group:
            mx, my = monster.get_position()
            adx = abs(mx - x)
            ady = abs(my - y)
            if (adx == 1 and ady == 0) or (adx == 0 and ady == 1):
                monster.set_position(x, y)
                return

    def render(self, surface):

        for ground in self.ground_group:
            ground.render_tile(surface)

        for wall in self.wall_group:
            wall.render_tile(surface)

        for coin in self.coin_group:
            if coin.visiable == True:
                coin.render_tile(surface)

        for monster in self.monster_group:
            monster.render_tile(surface)

        self.player.render_tile(surface)
        # pygame.time.wait(150)

        text_point = self.titleFont.render(
            str(self.game.state.get_score()) + " $", True, (100, 0, 0))
        surface.blit(text_point, (0, 0))

        if self.game.game_over:
            pygame.display.set_mode((GAME_SETTING.M_WIDTH, GAME_SETTING.M_HEIGHT))
            pygame.display.set_caption(GAME_SETTING.TITLE)
            pygame.display.set_icon(pygame.image.load(GAME_ICON))

            game_over = self.titleFont.render(
                "GAME OVER", True, (100, 0, 0))
            surface.blit(game_over, (70, 170))

            score = self.itemFont.render("Score: " + str(self.game.state.data.score), True, (100, 0, 0))
            surface.blit(score, (200, 275))


if __name__ == "__main__":
    pass
