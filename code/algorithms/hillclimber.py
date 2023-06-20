import copy


class HillClimber:
    def __init__(self, board, solution) -> None:

        if not board.is_won():
            raise Exception("HillClimber requires a solves board.")

        self.board = copy.deepcopy(board)
        self.solution = solution

    def get_new_solution(self):
        pass

    def go(self, iterations):
        print(f"solution: {self.solution}")

        self.iterations = iterations

        for iteration in range(iterations):
            pass