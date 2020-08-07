from GameState import GameState


def score_evaluation_func(current_game_state: GameState):
    return current_game_state.get_score()


class MiniMaxAgent:
    depth = 2

    def __init__(self, depth=2):
        self.depth = int(depth)

    def get_action(self, game_state: GameState):
        pacman_legal_actions = game_state.get_legal_actions(0)  # player
        max_value = float('-inf')
        max_action = None
        for action in pacman_legal_actions:
            min_successor = game_state.generate_successor(0, action)
            action_value = self.min_value(min_successor, 1, 0)
            if action_value > max_value:
                max_value = action_value
                max_action = action
        return max_action

    def max_value(self, game_state: GameState, depth: int):
        if depth == self.depth or len(game_state.get_legal_actions(0)) == 0:
            return score_evaluation_func(game_state)
        return max(
            [self.min_value(game_state.generate_successor(0, action), 1, depth) for action in
             game_state.get_legal_actions(0)]
        )

    def min_value(self, game_state: GameState, agent_index: int, depth: int):
        if len(game_state.get_legal_actions(agent_index)) == 0:
            return score_evaluation_func(game_state)

        if agent_index < game_state.get_num_agents() - 1:
            return min(
                [self.min_value(game_state.generate_successor(agent_index, action), agent_index + 1, depth) for action
                 in game_state.get_legal_actions(agent_index)])
        else:
            return min([self.max_value(game_state.generate_successor(agent_index, action), depth + 1) for action in
                        game_state.get_legal_actions(agent_index)])
