class Directions:
    #                   ^
    #                 South
    #      East <      STOP      West >
    #                 North
    #                 V
    UP = 'Up'
    DOWN = 'Down'
    RIGHT = 'Right'
    LEFT = 'Left'
    STOP = 'Stop'


class Actions:
    _directions = {Directions.DOWN: (0, 1),
                   Directions.UP: (0, -1),
                   Directions.RIGHT: (1, 0),
                   Directions.LEFT: (-1, 0)}

    _directionsAsList = _directions.items()

    @staticmethod
    def vector_to_direction(vector):
        dx, dy = vector
        if dy > 0:
            return Directions.DOWN
        if dy < 0:
            return Directions.UP
        if dx < 0:
            return Directions.LEFT
        if dx > 0:
            return Directions.RIGHT
        return Directions.STOP

    @staticmethod
    def direction_to_vector(direction, step=1):
        dx, dy = Actions._directions[direction]
        return (dx * step, dy * step)

    @staticmethod
    def get_possible_actions(point_direction, walls):
        possible_actions = []
        x, y = point_direction.get_position()
        wall_x, wall_y = walls.width, walls.height
        for dir, vector in Actions._directionsAsList:
            dx, dy = vector
            next_x = int(x+dx)
            next_y = int(y + dy)
            if next_x >= 0 and next_y >= 0 and next_x < wall_x and next_y < wall_y:
                if not walls[next_x][next_y]:
                    possible_actions.append(dir)
        return possible_actions

    @staticmethod
    def get_successor(position, action):
        dx, dy = Actions.direction_to_vector(action)
        x, y = position
        return (x+dx, y+dy)


class PointState:
    pos = (0, 0)
    direction = Directions.STOP

    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction

    def get_position(self) -> tuple:
        return self.pos

    def get_direction(self):
        return self.direction

    def is_integer(self):
        x, y = self.pos
        return x == int(x) and y == int(y)

    def __eq__(self, other):
        if other == None:
            return False
        return self.pos == other.pos and self.direction == other.direction

    def __str__(self):
        return "(x,y)=" + str(self.pos) + ", " + str(self.direction)

    def generate_successor(self, vector):
        x, y = self.pos
        dx, dy = vector
        direction = Actions.vector_to_direction(vector)
        if direction == Directions.STOP:
            direction = self.direction
        return PointState((x+dx, y+dy), direction)
