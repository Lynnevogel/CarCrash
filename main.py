from code.classes.cars import Car
from code.classes.rushhour import Rush_hour
from sys import argv
import random
import time


if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python rush_hour.py [game]")
        exit(1)

    game_name = argv[1]

    rushhour = Rush_hour(game_name)

    start_time = time.time()

    while not rushhour.is_won():
        random_car = rushhour.random_car()
        print(random_car)
        possible_coordinates = rushhour.can_move(random_car)
        print(f"huh: {possible_coordinates}")
        rushhour.move(random_car, possible_coordinates)
        rushhour.print_board()

        if rushhour.is_won():
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(elapsed_time)
            break
