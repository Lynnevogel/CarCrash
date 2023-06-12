from code.classes.rushhour import Rush_hour
from sys import argv
import time


if __name__ == "__main__":
    if len(argv) != 2:
        # raise error if game name is not given
        print("Usage: python main.py [game]")
        exit(1)

    # extract command line argument
    game_name = argv[1]
    # initialize game
    rushhour = Rush_hour(game_name)
    # start timer
    start_time = time.time()

    # run game until it is won
    while not rushhour.is_won():
        # pick a random car
        random_car = rushhour.random_car()
        # move car
        possible_coordinates = rushhour.can_move(random_car)
        rushhour.move(random_car, possible_coordinates)
        # print board
        rushhour.print_board()

        # check if game is won
        if rushhour.is_won():
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Puzzle was solved in {elapsed_time}s")
            break
