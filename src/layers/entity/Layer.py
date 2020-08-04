import pygame
from setting import GAME_SETTING
from pygame.math import Vector2
from gpath import *


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
            self.cell_size = Vector2(
                GAME_SETTING.TILE_SIZE, GAME_SETTING.TILE_SIZE)
        if image_file != None:
            self.layer_img = pygame.image.load(image_file)
            self.texture = pygame.transform.scale(
                self.layer_img, (32, 32))
        else:
            self.texture = pygame.Surface((32, 32))
            self.texture.fill(GAME_SETTING.GREEN)

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
        textureRect = pygame.Rect(0, 0, self.get_width, self.get_height)

        if angle is None:
            surface.blit(self.texture, (self.position.x * 32,
                                        self.position.y * 32), textureRect)

    def render(self, surface):
        raise NotImplementedError()

    def check_collision(self, entity, dx=0, dy=0):
        x, y = self.position.x + dx, self.position.y + dy
        if x == entity.position.x and y == entity.position.y:
            return True
        return False
