from code.classes.board import Board
from code.algorithms.random import random_move
from code.visualization.color_blocks import visualize_board
# from code.visualization.shiny import shiny
from code.algorithms.breadth_first import breadth_first
from code.algorithms.depth_first import DepthFirst
from sys import argv
import time


if __name__ == "__main__":
    if len(argv) < 2:
        # Raise error if game name is not given
        print("Usage: python main.py [game] [optional: [algorithm]]")
        exit(1)
    elif len(argv) == 2:
        algorithm = 'random'
    elif len(argv) == 3:
        algorithm = argv[2]

    # Extract command line argument
    game_name = argv[1]
    # Initialize game
    board = Board(game_name)
    # Counter
    num_moves = 0
    # Start timer
    start_time = time.time()

    depth_first = DepthFirst(board)
    depth_first.go()

    # Run game until it is won
    while not board.is_won():
        # Random algorithm
        if algorithm == 'random':
            # Pick a random car
            random_car = board.random_car()
            # Find possible boards
            copy_boards, can_move = board.get_possible_moves_2(board, random_car)

            if can_move:
                # Pick a random move
                board = random_move(copy_boards)
                board.print_board()
                num_moves += 1
            else:
                print("cannot move car")
        elif algorithm == 'bf':
            start_state = board
            breadth_first(start_state)
        elif algorithm == 'df':
            depth_first = DepthFirst(board)
            depth_first.go()

    end_time = time.time()
    elapsed_time = round((end_time - start_time), 4)
    print(f"Puzzle was solved in {elapsed_time}s.")
    print(f"Number of moves: {num_moves}")
    visualize_board(board.board, board.cars)
