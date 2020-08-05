from .GameStateData import GameStateData


class GameState:
    explored = set()
    data: GameStateData = None

    def get_and_reset_explored(self):
        temp = GameState.explored.copy()
        GameState.explored = set()
        return temp

    def get_legal_actions(self, agent_index=0):
        pass

    def generate_successor(self, agent_index, action):
        if self.is_win() or self.is_lose(): raise Exception('Can\'t generate a successor of a terminal state.')
        state = GameState(self)

    def __init__(self, prev_state=None):
        if prev_state != None:
            self.data = GameStateData()
        else:
            self.data = GameStateData()

    def get_pacman_state(self):
        """
        Returns an AgentState object for pacman (in game.py)

        state.pos gives the current position
        state.direction gives the travel vector
        """
        return self.data.agent_states[0].copy()

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
