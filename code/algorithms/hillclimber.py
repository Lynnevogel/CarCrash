import copy
from code.algorithms.random import Random


class HillClimber:
    def __init__(self, solved_board, starting_board, solution) -> None:

        if not solved_board.is_won():
            raise Exception("HillClimber requires a solves board.")

        self.solved_board = copy.deepcopy(solved_board)
        self.starting_board = copy.deepcopy(starting_board)
        self.solution = solution
        self.best_solution = len(self.solution)

    def get_new_solution(self):
        random_algorithm = Random(self.starting_board)
        new_solution = random_algorithm.go()
        return new_solution

    def go(self, iterations):
        self.iterations = iterations

        for iteration in range(iterations):
            new_solution = self.get_new_solution()

            if len(new_solution.directions) < self.best_solution:
                self.best_solution = len(new_solution.directions)
                self.solution = new_solution.directions

        print(f"new best solution: {self.best_solution}")
        print(f"new best directions: {self.solution}")
 