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


class Configuration:
    """
    A Configuration holds the (x,y) coordinate of a character, along with its
    traveling direction.

    The convention for positions, like a graph, is that (0,0) is the lower left corner, x increases
    horizontally and y increases vertically.  Therefore, north is the direction of increasing y, or (0,1).
    """

    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction

    def getPosition(self):
        return (self.pos)

    def getDirection(self):
        return self.direction

    def isInteger(self):
        x, y = self.pos
        return x == int(x) and y == int(y)

    def __eq__(self, other):
        if other == None:
            return False
        return (self.pos == other.pos and self.direction == other.direction)

    def __hash__(self):
        x = hash(self.pos)
        y = hash(self.direction)
        return hash(x + 13 * y)

    def __str__(self):
        return "(x,y)=" + str(self.pos) + ", " + str(self.direction)

    def generateSuccessor(self, vector):
        """
        Generates a new configuration reached by translating the current
        configuration by the action vector.  This is a low-level call and does
        not attempt to respect the legality of the movement.

        Actions are movement vectors.
        """
        x, y = self.pos
        dx, dy = vector
        direction = Actions.vectorToDirection(vector)
        if direction == Directions.STOP:
            direction = self.direction  # There is no stop direction
        return Configuration((x + dx, y + dy), direction)


class Actions:
    """
    A collection of static methods for manipulating move actions.
    """
    # Directions
    _directions = {Directions.DOWN: (0, 1),
                   Directions.UP: (0, -1),
                   Directions.RIGHT: (1, 0),
                   Directions.LEFT: (-1, 0)}
    # Directions.STOP: (0, 0)}

    _directionsAsList = _directions.items()

    def vectorToDirection(vector):
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

    vectorToDirection = staticmethod(vectorToDirection)

    def directionToVector(direction, speed=1.0):
        dx, dy = Actions._directions[direction]
        return (dx * speed, dy * speed)

    directionToVector = staticmethod(directionToVector)

    def getPossibleActions(config, walls):
        possible = []
        x, y = config.pos
        wall_x, wall_y = walls.width, walls.height
        for dir, vec in Actions._directionsAsList:
            dx, dy = vec
            next_y = int(y + dy)
            next_x = int(x + dx)
            if next_x >= 0 and next_y >= 0 and next_x < wall_x and next_y < wall_y:
                if not walls[next_x][next_y]:
                    possible.append(dir)

        return possible

    getPossibleActions = staticmethod(getPossibleActions)

    def getSuccessor(position, action):
        dx, dy = Actions.directionToVector(action)
        x, y = position
        return (x + dx, y + dy)

    getSuccessor = staticmethod(getSuccessor)

    def reverse_direction(action):
        if action == Directions.UP:
            return Directions.DOWN
        if action == Directions.DOWN:
            return Directions.UP
        if action == Directions.RIGHT:
            return Directions.LEFT
        if action == Directions.LEFT:
            return Directions.RIGHT
        return action
    reverse_direction = staticmethod(reverse_direction)


if __name__ == "__main__":
    wall_test = [
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]
    ]
    a = Configuration((4, 1), Directions.RIGHT)
    possible_action = Actions.getPossibleActions(a, wall_test)
    print(possible_action)
