from .GameStateData import GameStateData
from .GameState import GameState
from .Actions import *


class PacmanRules:
    PACMAN_SPEED = 1

    def get_legal_actions(state: GameState):
        return Actions.getPossibleActions(state.get_pacman_state(), state.data.layout.walls)

    get_legal_actions = staticmethod(get_legal_actions)

    def apply_action(state: GameState, action):
        legal = PacmanRules.get_legal_actions(state)
        if action not in legal:
            raise Exception("Illegal action " + str(action))

        pacman_state = state.data.agent_states[0]

        # Update Configuration
        vector = Actions.directionToVector(action, PacmanRules.PACMAN_SPEED)
        pacman_state.configuration = pacman_state.configuration.generateSuccessor(vector)

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
            if num_food == 0 and not state.data.lose:
                state.data.score_change += 500
                state.data.win = True

    consume = staticmethod(consume)
