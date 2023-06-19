from queue import PriorityQueue
from code.classes.board import Board

class AStar:
    def __init__(self, initial_state, heuristic):
        self.initial_state = initial_state
        

    def solve(self):
        open_set = PriorityQueue()
        # 0 -> zero heuristic 
        open_set.put((0, self.initial_state))
        closed_set = set()

        while not open_set.empty():
            _, current_state = open_set.get()

            if current_state.is_won():
                # Reached the goal state, return the solution path
                return self.reconstruct_path(current_state)

            closed_set.add(current_state)

            for successor in current_state.generate_successors():
                if successor in closed_set:
                    continue

                new_g_score = current_state.g_score + 1

                if not self.is_better_path(successor, new_g_score):
                    continue

                successor.g_score = new_g_score

                open_set.put((0, successor))  # Zero heuristic value

        # No solution found
        return None

    def is_better_path(self, state, new_g_score):
        # Check if the new path to the state is better than the existing path
        # You can use a data structure to track the best g_score for each state
        pass

    def reconstruct_path(self, state):
        path = []
        while state.parent is not None:
            path.append(state)
            state = state.parent
        path.append(self.initial_state)
        path.reverse()
        return path

