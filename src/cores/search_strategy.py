from search.bfs import *

from os import path
import os


class MazeGraph:
    map_encode = []
    row = 24
    col = 40
    map_file = "map.txt"
    map_data = []

    def __init__(self, map_file, row, col):
        self.map_file = map_file
        self.row = row
        self.col = col
        self.map_encode = []
        self.load_map()

    def load_map(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder,  self.map_file), 'rt') as f:
            for line in f:
                self.map_data.append(line)

        for row, tiles in enumerate(self.map_data, start=0):
            row_p = []
            for col, tile in enumerate(tiles, start=0):
                if tile in ['.', '1', '2', '3', 'P']:
                    row_p.append(tile)
            self.map_encode.append(row_p.copy())


class SearchStrategy:
    def __init__(self):
        pass


if __name__ == "__main__":
    print("Search startegy module")
    w = 40
    h = 24
    maze_graph = MazeGraph("map.txt", 24, 40)
    maze_problem = MazeProblem(
        maze_graph.map_encode, MazeState(12, 1), MazeState(24, 1))
    bfs = BFS()

    result, closed, cost = bfs.search(maze_problem, True)
    result_action_code = [rslt_item.actionCode for rslt_item in result]

    print("End module")
