import sys


class Action():
    actionCode = -1

    def __init__(self, code: int):
        self.actionCode = code


class State():
    def __init__(self):
        pass

    def isEquals(self):
        pass


class Expandable():
    cost = 0
    state = 0
    actionSequence = []

    def __init__(self):
        self.state = State()
        self.actionSequence = []
        self.cost = 0

    def setCost(self, val):
        self.cost = val

    def getCost(self):
        return self.cost


class Problem():

    def __init__(self):
        pass

    def result(self, s: State, a: Action):
        """[summary]
        Args:
            s (State): [description]
            a (Action): [description]
        Returns:
            List state
        """
        pass

    def actions(self, s: State):
        """[summary]

        Args:
            s (State): [description]
        Returns:
            List Action
        """
        pass

    def goalTest(self, s: State):
        """Test problem solved

        Args:
            s (State): [description]
        Return:
            True/False
        """
        pass

    def heuristic(self, s: State):
        """Heuristic func

        Args:
            s (State): [description]
        """
        pass


class MazeState(State):
    x = 0
    y = 0
    child = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_child(self, nodes: list):
        self.child = nodes.copy()

    def isEquals(self, state):
        return self.x == state.x and self.y == state.y


class MazeProblem(Problem):
    # overide
    start = 0
    goal = 0

    def __init__(self, graph, start: MazeState, goal: MazeState):
        self.start = start
        self.goal = goal
        self.graph = graph

    def initialState(self):
        return self.start

    def goalState(self):
        return self.goal
    # return list_action

    def actions(self, s: State):
        ms = s
        list_actions = []
        if ms.x > 0 and self.graph[ms.y][ms.x - 1] != '1':
            list_actions.append(Action(0))
        if ms.y > 0 and self.graph[ms.y-1][ms.x] != '1':
            list_actions.append(Action(1))
        if ms.x < 40 - 1 and self.graph[ms.y][ms.x + 1] != '1':
            list_actions.append(Action(2))
        if ms.y < 24 - 1 and self.graph[ms.y+1][ms.x] != '1':
            list_actions.append(Action(3))
        return list_actions

    # list_state
    def result(self, s: State, a: Action):
        # list_action = []
        # list_action.append(MazeState(a.actionCode, self.graph[a.actionCode]))
        ms = s
        rslt_state = []
        if a.actionCode == 0:
            rslt_state.append(MazeState(ms.x-1, ms.y))
        elif a.actionCode == 1:
            rslt_state.append(MazeState(ms.x, ms.y-1))
        elif a.actionCode == 2:
            rslt_state.append(MazeState(ms.x+1, ms.y))
        elif a.actionCode == 3:
            rslt_state.append(MazeState(ms.x, ms.y+1))
        return rslt_state

    def goalTest(self, s: State):
        return s.x == self.goal.x and s.y == self.goal.y


class BFS():
    def __init__(self):
        pass

    def search(self, p: Problem, isGraphSearch=False):
        """Algorithm search with problem

        Args:
            p (Problem): [description]
            isGraphSearch (bool, optional): [description]. Defaults to False.

        Returns:
            [type]: [description]
        """
        # frontier dfs_stack
        dfs_stack = []  # list  Expandable
        expaned_node = []  # explored

        # init start state
        init_expanable = Expandable()
        init_expanable.state = p.initialState()
        init_expanable.actionSequence = []
        dfs_stack.append(init_expanable)

        while(len(dfs_stack) > 0):
            s = dfs_stack.pop(0)
            #print("Pop {0} , {1}".format(s.state.x, s.state.y))
            if(p.goalTest(s.state)):
                expaned_node.append(s.state)
                # print("Goal reached")
                return s.actionSequence, expaned_node, len(expaned_node)
            else:
                expaned_node.append(s.state)

                for a in p.actions(s.state):
                    for target_state in p.result(s.state, a):

                        flag_add = True
                        if(isGraphSearch):
                            # check state in expaned
                            for expaned_state in expaned_node:
                                if expaned_state.isEquals(target_state):
                                    flag_add = False
                                    break

                        for openState in dfs_stack:
                            if openState.state.isEquals(target_state):
                                flag_add = False
                                break
                        if flag_add:
                            f_node = Expandable()
                            f_node.state = target_state

                            child_nodes = []  # array child actions
                            child_nodes = s.actionSequence.copy()
                            child_nodes.append(a)

                            f_node.actionSequence = child_nodes
                            dfs_stack.append(f_node)
        return False, False, False


def generate_graph():
    return []


# test_graph
if __name__ == "__main__":
    graph_neighbours = generate_graph()
    maze_problem = MazeProblem(graph_neighbours, '0', '61')
    bfs = BFS()
    result, closed, cost = bfs.search(maze_problem, True)

    if result is False and closed is False:
        print("No solution")
    else:
        result_str = [r.actionCode for r in result]
        explored_str = [s.label for s in closed]
        print("Path: ", result_str)
        print("Explored  ", explored_str)
        print("Cost ", explored_str)

    print("END program")
