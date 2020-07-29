from screens import GameScreen
import pygame
from global_path import *


class MenuScreen(GameScreen):
    def __init__(self):
        super(GameScreen, self).__init__()
        print("- Create Menu Screen")
        self.titleFont = pygame.font.Font(
            PATH_ASSETS + "font/BD_Cartoon_Shout.ttf", 72)
        self.itemFont = pygame.font.Font(
            PATH_ASSETS + "font/BD_Cartoon_Shout.ttf", 48)
        self.menuWidth = 0

        self.menuItems = [
            {
                'title': 'Level 1'
            },
            {
                'title': 'Level 2'
            },
            {
                'title': 'Level 3'
            },
            {
                'title': 'Setting'
            },
            {
                'title': 'Group Information'
            },
            {
                'title': 'Exit'
            }
        ]
        for item in self.menuItems:
            surface = self.itemFont.render(item['title'], True, (200, 0, 0))
            self.menuWidth = max(self.menuWidth, surface.get_width())
            item['surface'] = surface

        self.currentMenuItem = 0
        self.menuCursor = pygame.image.load(PATH_IMAGE + "icon.png")
        self.backgroundImage = pygame.image.load(PATH_IMAGE + "bg.jpg")

    def on_key_up(self, event):
        print("Key up handler")

    def on_mbutton_up(self, event):
        print("Click chuot trai", event.pos)

    def process_input(self):
        for event in pygame.event.get():
            self.on_event(event)
            if event.type == pygame.QUIT:
                # self.notifyQuitRequested
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notifyShowGameRequested()
                elif event.key == pygame.K_DOWN:
                    if self.currentMenuItem < len(self.menuItems) - 1:
                        self.currentMenuItem += 1
                elif event.key == pygame.K_UP:
                    if self.currentMenuItem > 0:
                        self.currentMenuItem -= 1
                elif event.key == pygame.K_RETURN:
                    menuItem = self.menuItems[self.currentMenuItem]
                    try:
                        menuItem['action']()
                    except Exception as ex:
                        print(ex)

    def render(self, window):
        window.blit(self.backgroundImage, (0, 0))
        y = 50
        surface = self.titleFont.render(
            "Pacman Modern AI", True, (200, 0, 0))
        x = (1280 - self.menuWidth) // 2
        window.blit(surface, (x, y))

        y += (200 * surface.get_height()) // 100

        # Draw menu items
        x = (window.get_width() - self.menuWidth) // 2
        for index, item in enumerate(self.menuItems):
            # Item text
            surface = item['surface']
            window.blit(surface, (x, y))

            # Cursor
            if index == self.currentMenuItem:
                cursorX = x - self.menuCursor.get_width() - 10
                cursorY = y + (surface.get_height() -
                               self.menuCursor.get_height()) // 2
                window.blit(self.menuCursor, (cursorX, cursorY))

            y += (120 * surface.get_height()) // 100
