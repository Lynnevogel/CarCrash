from code.classes.board import Board
from sys import argv
import time
from code.algorithms.random import random_move
from code.algorithms.breadth import breadth_first


if __name__ == "__main__":
    if len(argv) < 2:
        # Raise error if game name is not given
        print("Usage: python main.py [game]")
        exit(1)
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
        if algorithm == 'random' or len(argv) == 1:
            # Random algorithm
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
            # board.visualize_board()
            break
