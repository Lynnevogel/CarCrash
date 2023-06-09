import copy
from code.algorithms.random import Random
from code.classes.board import Board
from .breadth_first import BreadthFirst


class HillClimber(BreadthFirst):
    """
    Hillclimber algorithm.
    """
    def __init__(self, starting_board: "Board") -> None:
        """
        Initialize Hillclimber class and inherits the BreadFirst class.
        Precondtions:
        - board is a Board object of the current board
        """
        # Hill climber attributes
        self.starting_board = copy.deepcopy(starting_board)
        self.all_random_states: set[str] = set()
        # Breadth first attributes
        self.states = [copy.deepcopy(self.starting_board)]
        self.archive = {self.starting_board.get_representation(self.starting_board, "hillclimber")}
        self.number_of_moves: list[int] = []
        self.all_states = {self.starting_board.get_representation(self.starting_board, "hillclimber")}
        self.state_spaces: list[int] = []
        self.win_count = 0
        self.best_solution = []
        self.best_value = float('inf')
        self.depth_list: list[int] = []
        self.depth = 0

    def generate_new_random_solution(self) -> list[list[str|int]]:
        """
        Returns the directions of a random solution.
        Postconditions:
        - A nested list with a car and a direction is returned.
        """
        # Run random algorithm
        random_algorithm = Random(self.starting_board)
        new_random_solution = random_algorithm.go()
        # Get solution random algorithm
        new_random_solution = random_algorithm.board.order_solution()
        return new_random_solution

    def generate_random_solutions(self, iterations: int) -> None:
        """
        Generates x amount of random solutions and adds all possible states to a
        set, self.all_random_states.
        Precondition:
        - Amount of iterations as an integer
        """
        self.iterations = iterations

        # Checks for every iteration
        for _ in range(iterations):
            # Make copy of current board
            current_board = copy.deepcopy(self.starting_board)
            # Generates new solution
            new_random_solution = self.generate_new_random_solution()
            boards_random_solution = current_board.use_solution(current_board, new_random_solution)
            # Adds solution to set
            self.all_random_states.update(boards_random_solution)

    def add_all_possible_states(self, can_move: bool, moves: list["Board"]) -> None:
        """
        Adds states to the states list and keeps an archive of states that should not be
        added to the states list.
        Preconditions:
        - can_move is true of false
        - moves is a list with board objects
        """
        # If possible child states
        if can_move:
            # Loop through possibilities
            for move in moves:
                # Make a string of board
                move_representation = move.get_representation(move, "hillclimber")
                valid_move = self.check_move_in_all_random_states(move_representation)
                if move_representation not in self.archive and valid_move:
                    # Add to states
                    self.states.append(move)
                    # If not yet in archive, add to archive
                    self.archive.add(move_representation)

    def check_move_in_all_random_states(self, move_representation: str) -> bool:
        """
        Checks whether possible moves is in the possible states set.
        Precondition:
        - move_representation is a string
        Postcondition:
        - returns true if mvoe_representation is in all_random_states
        """
        return move_representation in self.all_random_states

    def run_iterations(self) -> None:
        """
        Iterates the random solutions and breadth first search
        an x amount of times.
        Precondition:
        - iterations is an integer
        """
        # Repeat for amount of iterations
        self.generate_random_solutions(3)
        # Start breadth-first search
        best_solution = self.go()
        self.best_solution = best_solution


    def generate_output(self) -> tuple[int, int, list[list[str|int]]]:
        """
        Return generated ouput from every run.
        Postconditions:
        - number_of_moves is the amount of moves made and is an integer.
        - number_of_states if the amound of states visited and is an integer.
        - solution is a nested list with a string and an integers.
        - state_space is an integers.
        """
        number_of_moves = len(self.best_solution)
        number_of_states = len(self.all_states)
        # Check length of best_solution for indexing
        solution = self.best_solution
        # Calculate max state space
        return number_of_moves, number_of_states, solution
