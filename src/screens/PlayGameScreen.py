from screens import GameScreen
import pygame
from global_path import *
from os import path
import pytweening as tween

TILESIZE = 32
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BGCOLOR = DARKGREY

# game settings
# 40x 24 = 960
WIDTH = 1280  # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12

BOB_RANGE = 20
BOB_SPEED = 0.6


class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        pygame.sprite.Sprite.__init__(self, self.groups)
        # self.image = pygame.Surface((TILESIZE, TILESIZE))
        land = pygame.image.load(PATH_IMAGE + "pacman.png")
        self.image = pygame.transform.scale(land, (TILESIZE, TILESIZE))
        # self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        # self.tween = tween.easeInOutSine
        # self.step = 0
        # self.dir = 1

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        # offset = BOB_RANGE * (self.tween(self.step / BOB_RANGE) - 0.5)
        # self.rect.y = self.y * TILESIZE + offset * self.dir
        # # self.rect. = self.y + offset * self.dir
        #
        # self.step += BOB_SPEED
        # if self.step > BOB_RANGE:
        #     self.step = 0
        #     self.dir *= -1


class Wall(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        # self.image = pygame.Surface((TILESIZE, TILESIZE))
        # self.image.fill(GREEN)
        self.game = game

        land = pygame.image.load(PATH_IMAGE + "land_1.png")
        self.image = pygame.transform.scale(land, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class PlayGameScreen(GameScreen):
    def __init__(self, state):
        GameScreen.__init__(self, state)
        print("- Create Play Game Screen")

        self.titleFont = pygame.font.Font(
            PATH_ASSETS + "font/BD_Cartoon_Shout.ttf", 72)
        self.itemFont = pygame.font.Font(
            PATH_ASSETS + "font/BD_Cartoon_Shout.ttf", 48)
        self.player = None
        self.load_data()
        self.new()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                elif tile == 'P':
                    self.player = Player(self, col, row)

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self, window):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(window, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(window, LIGHTGREY, (0, y), (WIDTH, y))

    def update(self):
        self.all_sprites.update()

    def on_key_down(self, event):
        if event.key == pygame.K_ESCAPE:
            self.quit()
        if event.key == pygame.K_LEFT:
            self.player.move(dx=-1)
            print('Left')
        if event.key == pygame.K_RIGHT:
            self.player.move(dx=1)
        if event.key == pygame.K_UP:
            self.player.move(dy=-1)
        if event.key == pygame.K_DOWN:
            self.player.move(dy=1)

    def process_input(self):
        for event in pygame.event.get():
            self.on_event(event)

    def render(self, window):

        window.fill(BGCOLOR)
        self.draw_grid(window)
        self.all_sprites.draw(window)
        pygame.display.flip()

    def clean(self):
        pass
