from code.classes.board import Board
from code.algorithms.random import random_move
from code.visualization.color_blocks import visualize_board
from sys import argv
import time
from code.algorithms.random import random_move
from code.algorithms.breadth import breadth_first


if __name__ == "__main__":
    if len(argv) < 2:
        # Raise error if game name is not given
        print("Usage: python main.py [game] [algorithm]")
        exit(1)
    elif len(argv) == 2:
        algorithm = 'random'
    elif len(argv) == 3:
        algorithm = argv[2]

    # Extract command line argument
    game_name = argv[1]
    # Initialize game
    board = Board(game_name)
    # Start timer
    start_time = time.time()
    # Counter
    num_moves = 0

    # Run game until it is won
    while not board.is_won():
        # Random algorithm
        if algorithm == 'random':
            # Pick a random car
            random_car = board.random_car()
            print(random_car)
            # Find possible coordinates
            copy_boards, true_or_false = board.can_move_car(random_car)
            print(copy_boards)

            if true_or_false == True:
                board = random_move(copy_boards)
                # Print board
                print("this is the chosen board:")
                board.print_board()
                # Count number of moves
                num_moves += 1
            else:
                print("cannot move car")
        elif algorithm == 'bf':
            
            start_state = board
            breadth_first(start_state)

        # Check if game is won
        if board.is_won():
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Puzzle was solved in {elapsed_time}s.")
            print(f"Number of moves: {num_moves}")
            visualize_board(board.board, board.cars)
            break
