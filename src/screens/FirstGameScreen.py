from screens import GameScreen
import pygame
from gpath import *
from os import path
import pytweening as tween
from layers.entity import Wall
from pygame.math import Vector2
from cores import FirstLevelManager
from states import *


class FirstGameScreen(GameScreen):
    def __init__(self, state):
        GameScreen.__init__(self, state=state)
        self.titleFont = pygame.font.Font(
            PATH_ASSETS + "font/BD_Cartoon_Shout.ttf", 72)
        self.itemFont = pygame.font.Font(
            PATH_ASSETS + "font/BD_Cartoon_Shout.ttf", 48)

        print("Created [play first level screen]")
        self.tile_manager = FirstLevelManager()

    def on_key_down(self, event):
        if event.key == pygame.K_ESCAPE:
            self.state.actionChangeActiveScreen(EScreenState.MENU)
        if event.key == pygame.K_p:
            self.tile_manager.start()
        if event.key == pygame.K_LEFT:
            self.tile_manager.move_player(dx=-1)
        if event.key == pygame.K_RIGHT:
            self.tile_manager.move_player(dx=1)
        if event.key == pygame.K_UP:
            self.tile_manager.move_player(dy=-1)
        if event.key == pygame.K_DOWN:
            self.tile_manager.move_player(dy=1)

    # def on_exit(self):
    #     print("End Game Now")

    def update(self):
        pass

    def render(self, window):
        window.fill((0, 0, 0))
        self.tile_manager.render(window)

    def clear(self):
        pass
