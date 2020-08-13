from .GameState import GameState
import random


def score_evaluation_func(current_game_state: GameState):
    return current_game_state.get_score()


class MiniMaxAgent:
    depth = 3

    def __init__(self, depth=3):
        self.depth = int(depth)

    def get_action(self, game_state: GameState):

        pacman_legal_actions = game_state.get_legal_actions(0)  # player
        max_value = float('-inf')
        max_action = None
        debug_value = []
        random_max = []
        for action in pacman_legal_actions:
            min_successor = game_state.generate_successor(0, action)
            action_value = self.min_value(min_successor, 1, 0)
            if action_value > max_value:
                max_value = action_value
                max_action = action
                random_max.clear()
                random_max.append(

                    (str(action),  max_value)

                )
            elif action_value == max_value:
                random_max.append(

                    (str(action),  max_value)

                )

            debug_value.append(
                {
                    (str(action),  max_value)
                }
            )

        if len(random_max) > 0:
            (kc, kv) = random.choice(random_max)
            return kc
        return max_action

    def max_value(self, game_state: GameState, depth: int):
        if depth == self.depth or len(game_state.get_legal_actions(0)) == 0:
            # print("Max_Value DEBUG : {0}, Depth{1}".format(

            #     score_evaluation_func(game_state),
            #     depth
            # ))
            return score_evaluation_func(game_state)

        return max(
            [self.min_value(game_state.generate_successor(0, action), 1, depth) for action in
             game_state.get_legal_actions(0)]
        )

    def min_value(self, game_state: GameState, agent_index: int, depth: int):
        if game_state.get_num_agents() == 1:
            return 0

        if len(game_state.get_legal_actions(agent_index)) == 0:
            # print("Min_Value DEBUG : {0}, Agent_index {1}, Depth{2}".format(
            #     score_evaluation_func(game_state),
            #     agent_index,
            #     game_state
            # ))
            return score_evaluation_func(game_state)

        if agent_index < game_state.get_num_agents() - 1:
            return min(
                [self.min_value(game_state.generate_successor(agent_index, action), agent_index + 1, depth) for action
                 in game_state.get_legal_actions(agent_index)])
        else:
            return min([self.max_value(game_state.generate_successor(agent_index, action), depth + 1) for action in
                        game_state.get_legal_actions(agent_index)])


class AlphaBetaAgent:
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    depth = 3

    def __init__(self, depth=3):
        self.depth = int(depth)

    def get_action(self, game_state: GameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """

        alpha = float('-inf')  # max best option on path to root
        beta = float('inf')  # min best option on path to root

        action_value = float('-inf')
        max_action = None
        debug_value = []
        random_max = []
        for action in game_state.get_legal_actions(0):  # get action of pacman
            action_value = self.Min_Value(
                game_state.generate_successor(0, action), 1, 0, alpha, beta)
            if (alpha < action_value):
                alpha = action_value
                max_action = action
                random_max.clear()
                random_max.append(

                    (str(action),  action_value)

                )
            elif alpha == action_value:
                random_max.append(

                    (str(action),  action_value)

                )

            debug_value.append(
                {
                    (str(action),  action_value)
                }
            )

        if len(random_max) > 0:
            (kc, kv) = random.choice(random_max)
            return kc
        return max_action

    def Min_Value(self, game_state, agent_index, depth, alpha, beta):
        """ For Min agents best move """
        if game_state.get_num_agents() == 1:
            return 0

        # No Legal actions.
        if (len(game_state.get_legal_actions(agent_index)) == 0):
            return score_evaluation_func(game_state)

        action_value = float('inf')
        for action in game_state.get_legal_actions(agent_index):
            if (agent_index < game_state.get_num_agents() - 1):
                action_value = min(action_value, self.Min_Value(game_state.generate_successor(
                    agent_index, action), agent_index + 1, depth, alpha, beta))
            else:  # the last ghost HERE
                action_value = min(action_value, self.Max_Value(
                    game_state.generate_successor(agent_index, action), depth + 1, alpha, beta))

            if (action_value < alpha):
                return action_value
            beta = min(beta, action_value)
        return action_value

    def Max_Value(self, gameState, depth, alpha, beta):
        """For Max agents best move"""

        if (depth == self.depth or len(gameState.get_legal_actions(0)) == 0):
            return score_evaluation_func(gameState)

        action_value = float('-inf')
        for action in gameState.get_legal_actions(0):
            action_value = max(action_value, self.Min_Value(
                gameState.generate_successor(0, action), 1, depth, alpha, beta))

            if (action_value > beta):
                return action_value
            alpha = max(alpha, action_value)

        return action_value
