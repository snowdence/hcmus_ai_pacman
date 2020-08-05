class GameStateData:

    def __init__(self, prev_state=None):
        if prev_state != None:
            self.foods = prev_state.food.shallowCopy()
            self.capsules = prev_state.capsules[:]
            self.agent_states = self.copy_agent_state(prev_state.agent_states)
            self.layout = prev_state.layout
            self._eaten = prev_state._eaten
            self.score = prev_state.score

        self._foodEaten = None
        self._foodAdded = None
        self._agentMoved = None
        self.lose = False
        self.win = False
        self.score_change = 0

    def deep_copy(self):
        state = GameStateData(self)
        state.food = self.foods.copy()  # deep copy
        state.layout = self.layout.copy()
        state._agentMoved = self._agentMoved
        state._foodEaten = self._foodEaten
        state._foodAdded = self._foodAdded

    def copy_agent_state(self, agent_states):
        copied_state = []
        for a_state in agent_states:
            copied_state.append(a_state.copy())
        return copied_state

    def initialize(self, layout, num_ghost_agents):
        self.foods = layout.food.copy()
        self.layout = layout
        self.score = 0
        self.score_change = 0
        self.agent_states = []
        num_ghosts = 0
        self._eaten = [False for a in self.agent_states]
