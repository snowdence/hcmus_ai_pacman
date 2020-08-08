from pygame.math import Vector2


class ScreenState:
    screen_size: Vector2 = None

    def __init__(self):
        pass

    @property
    def get_width(self):
        return int(self.screen_size.x)

    @property
    def get_height(self):
        return int(self.screen_size.y)

    def is_inside(self, position):
        return position.x >= 0 and position.y < self.get_width and position.y >= 0 and position.y < self.get_height

    def find_unit(self, position):
        for entity in self.entities:
            if int(entity.position.x) == int(position.x) and int(entity.position.y) == int(position.y):
                return entity
        return None
