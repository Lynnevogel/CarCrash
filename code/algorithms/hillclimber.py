import copy
from code.algorithms.random import Random
from code.classes.board import Board
from .breadth_first import BreadthFirst
from typing import Union


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
        self.archive = {self.starting_board.get_representation(self.starting_board)}
        self.number_of_moves: list[int] = []
        self.all_states = {self.starting_board.get_representation(self.starting_board)}
        self.state_spaces: list[int] = []
        self.win_count = 0
        self.best_solution = []
        self.best_value = float('inf')
        self.depth_list: list[int] = []
        self.depth = 0  

    def generate_new_random_solution(self) -> "Board":
        """
        Returns the directions of a random solution. 
        Postconditions:
        - A nested list with a car and a direction is returned.
        """
        # run random algorithm
        random_algorithm = Random(self.starting_board)
        new_random_solution = random_algorithm.go()
        # get solution random algorithm
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

        # checks for every iteration
        for _ in range(iterations):
            # make copy of current board
            current_board = copy.deepcopy(self.starting_board)
            # generates new solution
            new_random_solution = self.generate_new_random_solution()
            boards_random_solution = current_board.use_solution(current_board, new_random_solution)
            # adds solution to set
            self.all_random_states.update(boards_random_solution)

    def add_all_possible_states(self, can_move: bool, moves: list["Board"]) -> None:
        """
        Adds states to the states list and keeps an archive of states that should not be 
        added to the states list.
        Preconditions: 
        - can_move is true of false
        - moves is a list with board objects
        """
        # if possible child states
        if can_move:
            # loop through possibilities
            for move in moves:
                # make a string of board
                move_representation = move.get_representation_breadth(move)
                valid_move = self.check_move_in_all_random_states(move_representation)
                if move_representation not in self.archive and valid_move:
                    # add to states
                    self.states.append(move)
                    # if not yet in archive, add to archive
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

    def run_iterations(self, iterations: int) -> None:
        """
        Iterates the random solutions and breadth first search an x amount of times.
        Precondition: 
        - iterations is an integer
        """
        
        # repeat for amount of iterations
        for _ in range(iterations):
            self.generate_random_solutions(5)
            # add state so breadth first can start
            self.states = [copy.deepcopy(self.starting_board)]
            self.archive = {self.starting_board.get_representation(self.starting_board)}
            self.all_states = {self.starting_board.get_representation(self.starting_board)}
            # start breadth-first search
            best_solution = self.go()
            self.check_for_best_solution(best_solution)
            # Add statespace of solution to list
            self.state_spaces.append(len(self.all_random_states))


    def check_for_best_solution(self, solution: list[list[str|int]]) -> None:
        """
        Checks if new solution if better than previous best solution.
        Precondition: 
        - solution is a nested list with a string and an integer
        """
        # get length of solutions
        current_best_solution = len(self.best_solution)
        new_solution = len(solution)

        # compare solutions and change new best solution
        if new_solution < current_best_solution:
            self.best_solution = solution
            self.number_of_moves = len(new_solution)

    def generate_output(self) -> tuple[int, int, list[list[str|int]], int]:
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
        # check length of best_solution for indexing
        if len(self.best_solution) > 1:
            solution = self.best_solution
        else:
            solution = self.best_solution[0]
            number_of_moves = len(self.best_solution[0])
        # calculate max state space
        state_space = max(self.state_spaces) + 1
        return number_of_moves, number_of_states, solution, state_space
