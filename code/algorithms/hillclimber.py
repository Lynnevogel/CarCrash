import copy
from code.algorithms.random import Random
from code.classes.board import Board
from .breadth_first import BreadthFirst
from typing import Any, Optional


class HillClimber(BreadthFirst):
    def __init__(self, starting_board) -> None:
        self.starting_board = copy.deepcopy(starting_board)
        self.all_random_states = set()
        # breadth first attributes
        self.states = [copy.deepcopy(self.starting_board)]
        self.archive = {self.starting_board.get_representation(self.starting_board)}
        self.number_of_moves = []
        self.best_solution = []
        self.best_value = float('inf')
        self.depth_list = []
        self.depth = 0  

    def generate_new_random_solution(self):
        """
        Returns the directions of a random solution. 
        (The directions are a nested list with a car and a direction.)
        """
        random_algorithm = Random(self.starting_board)
        new_random_solution = random_algorithm.go()
        new_random_solution = new_random_solution.directions
        return new_random_solution

    def generate_random_solutions(self, iterations):
        """
        Generates x amount of random solutions and adds all possible states to a
        set, self.all_random_states. 
        """
        self.iterations = iterations

        for iteration in range(iterations):
            current_board = copy.deepcopy(self.starting_board)
            new_random_solution = self.generate_new_random_solution()
            boards_random_solution = current_board.use_solution(current_board, new_random_solution)
            self.all_random_states.update(boards_random_solution)
        
        print(f"all random states: {self.all_random_states}, {len(self.all_random_states)}")

    def add_all_possible_states(self, new_board, can_move: bool, moves: list[Any]) -> None:
        """
        Adds states to the states list and keeps an archive of states that should not be 
        added to the states list.
        """
        if can_move:
            for move in moves:
                move_representation = move.get_representation_breadth(move)
                valid_move = self.check_move_in_all_random_states(move_representation)
                print(valid_move)
                if move_representation not in self.archive and valid_move:
                    self.states.append(move)
                    self.archive.add(move_representation)

    def check_move_in_all_random_states(self, move_representation):
        """
        Checks whether possible moves is in the possible states set.
        """
        return move_representation in self.all_random_states

    def run_iterations(self, iterations):
        for _ in range(iterations):
            self.generate_random_solutions(3)
            self.go()
            self.all_random_states = set()
