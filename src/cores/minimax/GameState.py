from GameStateData import GameStateData
from rules import *
from Actions import *


class GameState:
    explored = set()
    data: GameStateData = None

    def get_and_reset_explored(self):
        temp = GameState.explored.copy()
        GameState.explored = set()
        return temp

    def get_legal_actions(self, agent_index=0):
        if self.is_win() or self.is_lose():
            return []

        if agent_index == 0:
            return PacmanRules.get_legal_actions(self)
        else:
            return GhostRules.get_legal_action(self, agent_index)

    def generate_successor(self, agent_index, action):
        if self.is_win() or self.is_lose():
            raise Exception('Can\'t generate a successor of a terminal state.')
        state = GameState(self)

        if agent_index == 0:
            PacmanRules.apply_action(state, action)
        else:
            GhostRules.apply_action(state, action, agent_index)

        if agent_index == 0:
            state.data.score_change += -1

        state.data.agentMoved = agent_index
        state.data.score += state.data.score_change

        GameState.explored.add(self)
        GameState.explored.add(state)
        return state

    def __init__(self, prev_state=None):
        if prev_state != None:
            self.data = GameStateData(prev_state.data)
        else:
            self.data = GameStateData()

    def get_num_agents(self):
        num = len(self.data.agent_states)
        return num

    def get_pacman_state(self):
        return self.data.agent_states[0].copy()

    def get_ghost_states(self):
        return self.data.agent_states[1:]

    def get_score(self):
        return float(self.data.score)

    def get_num_food(self):
        return self.data.foods.count()

    def get_food(self):
        return self.data.foods

    def has_food(self, x: int, y: int):
        return self.data.foods[x][y]

    def is_win(self):
        return self.data.win

    def is_lose(self):
        return self.data.lose

    def initialize(self, layout, numGhostAgents=1000):
        """
        Creates an initial game state from a layout array (see layout.py).
        """
        self.data.initialize(layout, numGhostAgents)
        print("ok")

    def deepcopy(self):
        state = GameState(self)
        state.data = self.data.deepcopy()
        return state

    def get_ghost_state(self, agent_index):
        if agent_index == 0 or agent_index >= self.get_num_agents():
            raise Exception("Invalid index passed to getGhostState")
        return self.data.agent_states[agent_index]


class PacmanRules:
    PACMAN_SPEED = 1

    def get_legal_actions(state: GameState):
        return Actions.getPossibleActions(state.get_pacman_state().configuration, state.data.layout.walls)

    get_legal_actions = staticmethod(get_legal_actions)

    def apply_action(state: GameState, action):
        legal = PacmanRules.get_legal_actions(state)
        if action not in legal:
            raise Exception("Illegal action " + str(action))

        pacman_state = state.data.agent_states[0]

        # Update Configuration
        vector = Actions.directionToVector(action, PacmanRules.PACMAN_SPEED)
        pacman_state.configuration = pacman_state.configuration.generateSuccessor(
            vector)

        # eat
        next = pacman_state.configuration.getPosition()
        PacmanRules.consume(next, state)

    apply_action = staticmethod(apply_action)

    def consume(position, state: GameState):
        x, y = position
        if state.data.foods[x][y]:
            state.data.score_change += 20
            state.data.foods = state.data.foods.copy()
            state.data.foods[x][y] = False  # eat

            state.data.food_eaten = position

            num_food = state.get_num_food()
            #print("Current food {0}".format(num_food))
            #print("Current score {0}".format(state.data.score))
            if num_food == 0 and not state.data.lose:
                state.data.score_change += 500
                state.data.win = True

    consume = staticmethod(consume)


class GhostRules:
    GHOST_SPEED = 1.0

    def get_legal_action(state: GameState, ghost_index):
        conf = state.get_ghost_state(ghost_index).configuration
        able_actions = Actions.getPossibleActions(
            conf, state.data.layout.walls)
        if Directions.STOP in able_actions:
            able_actions.remove(Directions.STOP)  # not allow ghost stop
        #  process rotate 180 (not allow)
        return able_actions

    get_legal_action = staticmethod(get_legal_action)

    def apply_action(state: GameState, action, ghost_index):
        legal = GhostRules.get_legal_action(state, ghost_index)
        if action not in legal:
            raise Exception("Illegal ghost action" + str(action))

        ghost_state = state.data.agent_states[ghost_index]
        vector = Actions.directionToVector(action, 1.0)
        ghost_state.configuration = ghost_state.configuration.generateSuccessor(
            vector)

    apply_action = staticmethod(apply_action)
