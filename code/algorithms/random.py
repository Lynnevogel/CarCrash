from code.classes.board import Board
import random


class Random:
    def __init__(self, board: "Board") -> None:
        """
        Initialize Random class with current board and counter
        for number of moves.
        Preconditions:
        - board is a Board object with the current board.
        """
        self.board = board
        self.num_moves = 0

    def random_move(self, possible_boards: list[Board]) -> "Board":
        """
        Chooses a random board from the possible board, if list is not empty.
        Preconditions:
        - possible_boards is a list of Board objects, that
        are possible state from the current board.
        Postconditions:
        - A random chosen board is returned.
        """
        if len(possible_boards) == 0:
            return None
        else:
            return random.choice(possible_boards)

    def go(self) -> "Board":
        # Run game until it is won
        while not self.board.is_won():
            # Pick a random car
            random_car = self.board.random_car()
            # Find possible boards, when moving the random chosen car
            copy_boards, can_move = self.board.get_possible_moves(self.board, random_car)

            if can_move:
                # Pick a random move
                self.board = self.random_move(copy_boards)
                # self.board.print_board()
                # visualize_board(board.board, board.cars, save_path=f"code/visualization/board_images/board{num_moves}.png")
                self.num_moves += 1
            else:
                print("cannot move car")
            print(f"number of moves: {self.num_moves}")

        return self.board

    def generate_output(self) -> tuple[int, int, list[list[str | int]]]:
        """
        Return generated ouput from every run.
        Postconditions:
        - number_of_moves is the amount of moves made and is an integer.
        - number_of_states if the amound of states visited and is an integer.
        - solution is a nested list with a string and an integers.
        """
        number_of_moves = self.num_moves
        number_of_states = self.num_moves
        solution = self.board.directions
        return number_of_moves, number_of_states, solution
