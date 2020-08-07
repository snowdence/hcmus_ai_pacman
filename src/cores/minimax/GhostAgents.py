from Agent import Agent
from Actions import *
from util import *
from GameState import GameState


class GhostAgent(Agent):
    def __init__(self, index):
        super(GhostAgent, self).__init__()
        self.index = index

    def get_action(self, state):
        dist = self.get_distribution(state)
        if len(dist) == 0:
            return Directions.STOP
        else:
            return chooseFromDistribution(dist)

    def get_distribution(self, state: GameState):
        dist = Counter()
        for a in state.get_legal_actions(self.index):
            dist[a] = 1.0
        dist.normalize()
        return dist
