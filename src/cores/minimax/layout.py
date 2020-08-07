from Grid import Grid
import os
import random


class Layout:
    def __init__(self, layout_arr):
        self.layout_arr = layout_arr
        self.width = len(layout_arr[0])
        self.height = len(layout_arr)
        self.walls = Grid(self.width, self.height, False)
        self.foods = Grid(self.width, self.height, False)

        self.agent_positions = []
        self.num_ghosts = 0
        self.process_layout_text(layout_arr)

        self.total_food = len(self.foods.asList())
        print("Init layout")

    def get_num_ghosts(self):
        return self.num_ghosts

    def is_wall(self, pos):
        x, col = pos
        return self.walls[x][col]

    def __str__(self):
        return "\n".join(self.layout_arr)

    def deepcopy(self):
        return Layout(self.layout_arr[:])

    def process_layout_text(self, layout_arr):
        """
               Coordinates are flipped from the input format to the (x,y) convention here

               The shape of the maze.  Each character
               represents a different type of object.
                % - Wall
                . - Food
                o - Capsule
                G - Ghost
                P - Pacman
               Other characters are ignored.
               """
        max_y = self.height - 1
        for y in range(self.height):
            for x in range(self.width):
                layout_char = layout_arr[max_y - y][x]
                self.process_layout_char(x, y, layout_char)
        self.agent_positions.sort()
        self.agent_positions = [(i == 0, pos) for i, pos in self.agent_positions]

    def process_layout_char(self, x, y, layout_char):
        if layout_char == '1':
            self.walls[x][y] = True
        elif layout_char == '.':
            self.foods[x][y] = True
        elif layout_char == 'P':
            self.agent_positions.append((0, (x, y)))
        elif layout_char in ['3']:
            self.agent_positions.append((1, (x, y)))
            self.num_ghosts += 1


def try_load(fullname):
    if not os.path.exists(fullname):
        return None
    f = open(fullname)
    try:
        return Layout([line.strip() for line in f])
    finally:
        f.close()


def get_layout(name='map.txt'):
    layout = try_load(name)
    return layout


if __name__ == "__main__":
    test_get_layout = get_layout('map.txt')
    print(test_get_layout)
    # pass
