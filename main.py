from code.classes.board import Board
from sys import argv
import time
from code.algorithms.random import random_move


if __name__ == "__main__":
    if len(argv) != 2:
        # Raise error if game name is not given
        print("Usage: python main.py [game]")
        exit(1)

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
        # Pick a random car
        random_car = board.random_car()
        # Find possible coordinates
        possible_coordinates = board.can_move(random_car)
        # Choice movement
        move = random_move(possible_coordinates)
        # Move car
        board.move(random_car, move)
        # Print board
        board.print_board()
        # Count number of moves
        num_moves += 1

        # Check if game is won
        if board.is_won():
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Puzzle was solved in {elapsed_time}s.")
            print(f"Number of moves: {num_moves}")
            print(type(board.board))
            board.visualize_board()
            break
