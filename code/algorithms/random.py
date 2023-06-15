import random

def random_move(possible_boards: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # Check length of the list with possible coordinates/moves
    # if len(possible_boards) == 0:
    #     print("Cannot move car.")
    # elif len(possible_boards) != 0:
    #     # Move car to new coordinates
    #     new_car_coordinates = random.choice(possible_boards)

    return random.choice(possible_boards)
