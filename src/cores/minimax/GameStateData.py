from .Actions import *


class AgentState:
    """
    AgentStates hold the state of an agent (configuration, speed, scared, etc).
    """

    def __init__(self, startConfiguration, isPacman):
        self.start = startConfiguration
        self.configuration = startConfiguration
        self.isPacman = isPacman
        self.scaredTimer = 0
        self.numCarrying = 0
        self.numReturned = 0

    def __str__(self):
        if self.isPacman:
            return "Pacman: " + str(self.configuration)
        else:
            return "Ghost: " + str(self.configuration)

    def __eq__(self, other):
        if other == None:
            return False
        return self.configuration == other.configuration

    def __hash__(self):
        return hash(hash(self.configuration) + 13 * hash(self.scaredTimer))

    def copy(self):
        state = AgentState(self.start, self.isPacman)
        state.configuration = self.configuration
        state.scaredTimer = self.scaredTimer
        state.numCarrying = self.numCarrying
        state.numReturned = self.numReturned
        return state

    def getPosition(self):
        if self.configuration == None:
            return None
        return self.configuration.getPosition()

    def getDirection(self):
        return self.configuration.getDirection()


class GameStateData:

    def __init__(self, prev_state=None):
        if prev_state != None:
            self.foods = prev_state.foods.shallow_copy()
            self.agent_states = self.copy_agent_state(prev_state.agent_states)
            self.layout = prev_state.layout
            self.eaten = prev_state.eaten
            self.score = prev_state.score
        self.foodEaten = None
        self.foodAdded = None
        self.agentMoved = None
        self.lose = False
        self.win = False
        self.score_change = 0

    def deepcopy(self):
        state = GameStateData(self)
        state.foods = self.foods.deepcopy()  # deep copy
        state.layout = self.layout.deepcopy()
        state.agentMoved = self.agentMoved
        state.foodEaten = self.foodEaten
        state.foodAdded = self.foodAdded
        return state

    def copy_agent_state(self, agent_states):
        copied_state = []
        for a_state in agent_states:
            copied_state.append(a_state.copy())
        return copied_state

    def initialize(self, layout, num_ghost_agents):
        self.foods = layout.foods.shallow_copy()
        self.layout = layout
        self.score = 0
        self.score_change = 0
        self.agent_states = []
        num_ghosts = 0
        self.eaten = [False for a in self.agent_states]

        num_ghost = 0
        for isPacman, pos in layout.agent_positions:
            if not isPacman:
                if num_ghost == num_ghost_agents:
                    continue  # Max ghosts reached already
                else:
                    num_ghost += 1
            self.agent_states.append(AgentState(
                Configuration(pos, Directions.STOP), isPacman))
        self._eaten = [False for a in self.agent_states]
