import sys
from cores.agent import *


class BFS:
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

        while (len(dfs_stack) > 0):
            s = dfs_stack.pop(0)
            # print("Pop {0} , {1}".format(s.state.x, s.state.y))
            if (p.goalTest(s.state)):
                expaned_node.append(s.state)
                # print("Goal reached")
                return s.actionSequence, expaned_node, len(expaned_node)
            else:
                expaned_node.append(s.state)

                for a in p.actions(s.state):
                    for target_state in p.result(s.state, a):

                        flag_add = True
                        if (isGraphSearch):
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
