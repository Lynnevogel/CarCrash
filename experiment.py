import time
import csv
import subprocess


def run_experiment(game_name: str, algorithm: str, amount_of_times: str) -> None:
    """
    Runs experiment by executing the main.py script with the specified arguments.
    Preconditions:
    - game_name is a string
    - algorithm is a string
    - amount_of_times is an integer
    """
    command = f"python3 main.py {game_name} {algorithm} {amount_of_times}"
    subprocess.run(command, shell=True)


def output_experiment(n: int, game: str, algorithm: str, dimension: int, time: float, number_of_moves: int, number_of_states: int, solution: list[list[str|int]]) -> None:
    """
    Writes the solution for a board into a CSV file.
    Preconditions:
    - n is an integer representing the experiment number
    - game is a string
    - algorithm is a string
    - dimension is an integer
    - time is a float representing the seconds one run took
    - number_of_moves is an integer
    - number_of states is an integer
    - won is a boolean
    - solution is a nested list with a string (car_key) and an integer (direction).
    - state_space is an optional string
    """
    # Open a new CSV file
    with open(f"output/experiment_output_{game}_{algorithm}_{n}_{time}.csv", "w") as file:
        writer = csv.writer(file)
        field = ["n", "game", "algorithm", "dimension", "time", "number of moves", "number of states", "solution: car", "solution: direction"]

        writer.writerow(field)
        # Add output to CSV file
        for move in solution:
            car_key = move[0]
            direction = move[1]
            writer.writerow([n, game, algorithm, dimension, time, number_of_moves, number_of_states, car_key, direction])


def start_time() -> float:
    """
    Initiates times.
    Postconditions:
    - Returns the current time in seconds.
    """
    start = time.time()
    return start


def end_time(start: float) -> float:
    """
    Calculates the elapsed time since the start time.
    Preconditions:
    - starttime is a float.
    Postconditions:
    - A float containing the elapsed time is returned.
    """
    # Get end time
    end = time.time()
    # Calculate change in time
    elapsed_time = round((end - start), 6)
    return elapsed_time


if __name__ == "__main__":
    game_name = "9x9_5"
    algorithm = "hillclimber"
    amount_of_times = "3"
    run_experiment(game_name, algorithm, amount_of_times)
