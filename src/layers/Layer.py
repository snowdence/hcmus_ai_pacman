import pygame
from setting import GAME_SETTING
from pygame.math import Vector2
from global_path import *


class Layer:
    tile_size = Vector2()  # use vector as size
    texture: pygame.Surface = None
    position = Vector2()

    def __init__(self, position=None, cell_size=None, image_file=None):
        if position != None:
            self.position = position
        else:
            self.position = Vector2(0, 0)

        self.cell_size = cell_size
        if cell_size != None:
            self.cell_size = cell_size
        else:
            self.cell_size = Vector2(GAME_SETTING.TILE_SIZE, GAME_SETTING.TILE_SIZE)
        if image_file != None:
            self.texture = pygame.image.load(image_file)
        else:
            self.texture = pygame.Surface((self.tile_size.x, self.tile_size.y))
            self.layer_img = pygame.image.load(image_file)
            self.layer_img_scaled = pygame.transform.scale(self.layer_img, (32, 32))

    def set_position(self, x, y):
        self.position = Vector2(x, y)

    @property
    def get_width(self):
        return int(self.cell_size.x)

    @property
    def get_height(self):
        return int(self.cell_size.y)

    def render_tile(self, surface, position=None, angle=None):
        if (position != None):
            self.position = position

        # spritePoint = self.position.elementwise() * self.cell_size

        # texturePoint = tile.elementwise() * self.cell_size
        textureRect = pygame.Rect(int(self.position.x), int(self.position.y), self.get_width, self.get_height)

        if angle is None:
            surface.blit(self.texture, (self.position.x * 32, self.position.y * 32), textureRect)

    def render(self, surface):
        raise NotImplementedError()
