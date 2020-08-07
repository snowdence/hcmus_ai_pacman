from GameState import GameState
from GameStateData import GameStateData
from rules import *
from MiniMaxAgent import MiniMaxAgent
from layout import *
from GhostAgents import GhostAgent


class Game:
    state: GameState = None

    def __init__(self, agents, rules, start_index=0):
        self.rules = rules
        self.agents = agents
        self.start_index = start_index
        self.move_history = []
        self.game_over = False
        self.total_agent_times = [0 for agent in agents]
        self.num_moves = 0

    def run(self):
        self.num_moves = 0
        agent_index = self.start_index
        num_agents = len(self.agents)
        while not self.game_over:

            agent = self.agents[agent_index]

            action = None
            observation = self.state.deepcopy()
            action = agent.get_action(observation)
            self.move_history.append((agent_index, action))
            self.state = self.state.generate_successor(agent_index, action)
            self.rules.process(self.state, self)

            print("Epoch agent {0}, Num moves{1}".format(
                agent_index, self.num_moves))

            if agent_index == num_agents - 1:
                self.num_moves += 1

            if agent_index == num_agents - 1:
                agent_index = 0
            else:
                agent_index += 1
            # display update
        print("End ")


class MinimaxProblem:
    game_over = False
    init_state: GameState = None

    def __init__(self):
        pass

    def new_game(self, layout, pacman_agent, ghost_agents):
        agents = [pacman_agent] + ghost_agents[:layout.get_num_ghosts()]
        init_state = GameState()
        init_state.initialize(layout, len(ghost_agents))

        game = Game(agents, self, 0)
        game.state = init_state
        self.init_state = init_state.deepcopy()
        game.run()
        return game

    def process(self, state: GameState, game):
        if state.is_win():
            game.game_over = True
        if state.is_lose():
            game.game_over = True


def run():
    minimax_problem = MinimaxProblem()
    num_ghost = 2
    layout = get_layout("map.txt")
    pacman = MiniMaxAgent()
    ghosts = [GhostAgent(i + 1) for i in range(num_ghost)]
    minimax_problem.new_game(layout, pacman, ghosts)

    print("Running")


run()
