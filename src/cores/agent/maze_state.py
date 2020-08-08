class MazeState:
    x: int = 0
    y: int = 0

    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    def isEquals(self, state) -> bool:
        return self.x == state.x and self.y == state.y
