from code.classes.board import Board
from typing import Union
import random
from code.visualization.color_blocks import visualize_board

class Random:
    def __init__(self, board) -> None:
        self.board = board

    def random_move(self, possible_boards: list[Board]) -> Union[Board, None]:
        if len(possible_boards) == 0:
            return None
        else:
            return random.choice(possible_boards)
        
    def go(self):
        num_moves = 0
        # Run game until it is won
        while not self.board.is_won():
            # Pick a random car
            random_car = self.board.random_car()
            # Find possible boards
            copy_boards, can_move = self.board.get_possible_moves_2(self.board, random_car)

            if can_move:
                # Pick a random move
                self.board = self.random_move(copy_boards)
                # self.board.print_board()
                # visualize_board(board.board, board.cars, save_path=f"code/visualization/board_images/board{num_moves}.png")
                num_moves += 1
            else:
                print("cannot move car")
        print(f"number of moves: {num_moves}")
        # visualize_board(self.board.board, self.board.cars, None)

        # print(f"directions: {self.board.directions}")
        self.board.output(self.board.directions)
        return self.board
