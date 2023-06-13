import random

def random_move(possible_coordinates: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # Check length of the list with possible coordinates/moves
    if len(possible_coordinates) == 0:
        print("Cannot move car.")
        new_car_coordinates = []
    elif len(possible_coordinates) != 0:
        # Move car to new coordinates
        new_car_coordinates = random.choice(possible_coordinates)
    
    return new_car_coordinates
