from code.classes.rushhour import Rush_hour
from sys import argv
import time


if __name__ == "__main__":
    if len(argv) != 2:
        # Raise error if game name is not given
        print("Usage: python main.py [game]")
        exit(1)

    # Extract command line argument
    game_name = argv[1]
    # Initialize game
    rushhour = Rush_hour(game_name)
    # Start timer
    start_time = time.time()
    # Counter
    num_moves = 0

    # Run game until it is won
    while not rushhour.is_won():
        # Pick a random car
        random_car = rushhour.random_car()
        # Move car
        possible_coordinates = rushhour.can_move(random_car)
        rushhour.move(random_car, possible_coordinates)
        # Print board
        rushhour.print_board()
        # Count number of moves
        num_moves += 1

        # Check if game is won
        if rushhour.is_won():
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Puzzle was solved in {elapsed_time}s.")
            print(f"Number of moves: {num_moves}")
            print(type(rushhour.board))
            rushhour.visualize_board()
            break
