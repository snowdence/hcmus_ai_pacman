from screens import GameScreen
import pygame
from gpath import *
from os import path
import pytweening as tween
from layers.entity import Wall
from pygame.math import Vector2
from cores import TileManager, MinimaxManager
from states import *

from cores.minimax.GameState import GameState
from cores.minimax.GameStateData import GameStateData
from cores.minimax.rules import *
from cores.minimax.MiniMaxAgent import MiniMaxAgent, AlphaBetaAgent
from cores.minimax.layout import *
from cores.minimax.GhostAgents import GhostAgent, DirectionalGhost


class Game:
    state: GameState = None

    def __init__(self, agents, rules, start_index=0):
        self.rules = rules
        self.agents = agents
        self.start_index = start_index
        self.move_history = []
        self.game_over = False
        self.total_agent_times = [0 for agent in agents]
        self.num_moves = 0


class FourthGameScreen(GameScreen):
    game_over = False
    init_state: GameState = None

    def __init__(self, state):
        GameScreen.__init__(self, state=state)
        self.titleFont = pygame.font.Font(
            PATH_ASSETS + "font/BD_Cartoon_Shout.ttf", 72)
        self.itemFont = pygame.font.Font(
            PATH_ASSETS + "font/BD_Cartoon_Shout.ttf", 48)

        print("Created [Level 4 screen]")
        self.run()

    def new_game(self, layout, pacman_agent, ghost_agents):
        agents = [pacman_agent] + ghost_agents[:layout.get_num_ghosts()]
        init_state = GameState()
        init_state.initialize(layout, len(ghost_agents))

        game = Game(agents, self, 0)
        game.state = init_state
        self.init_state = init_state.deepcopy()
        return game

    def process(self, state: GameState, game):
        if state.is_win():
            game.game_over = True
        if state.is_lose():
            game.game_over = True

    def run(self):
        num_ghost = 2
        layout = get_layout("maps/mini.txt")
        pacman = MiniMaxAgent(2)
        ghosts = [GhostAgent(i + 1) for i in range(num_ghost)]
        game = self.new_game(layout, pacman, ghosts)
        self.tile_manager = MinimaxManager(game)

        print("Running")

    def on_key_down(self, event):
        if event.key == pygame.K_p:
            print("Play press!!!!")
            self.tile_manager.run()
        if event.key == pygame.K_LEFT:
            self.tile_manager.move_player(dx=-1)
        if event.key == pygame.K_RIGHT:
            self.tile_manager.move_player(dx=1)
        if event.key == pygame.K_UP:
            self.tile_manager.move_player(dy=-1)
        if event.key == pygame.K_DOWN:
            self.tile_manager.move_player(dy=1)

    def update(self):
        self.tile_manager.update()

    def render(self, window):
        window.fill((0, 0, 0))
        self.tile_manager.render(window)

    def clear(self):
        pass
