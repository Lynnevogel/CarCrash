from code.algorithms.random import Random
import time
import csv
import subprocess

def run_experiment(game_name, algorithm, amount_of_times):
    command = f"python3 main.py {game_name} {algorithm} {amount_of_times}"
    subprocess.run(command, shell=True)


def output_experiment(n, game, algorithm, dimension, time, number_of_moves, number_of_states, won, solution: list[list[str]], state_space=None) -> None:
    """
    Writes a solution for a board into a csv file.
    """
    with open(f"output/experiment_output_{game}_{algorithm}_{n}_{time}.csv", "w") as file:
        writer = csv.writer(file)
        field = ["n", "game", "algorithm", "dimension", "time", "number of moves", "number of states", "won", "state space", "solution: car", "solution: direction"]

        writer.writerow(field)

        for move in solution:
            car_key = move[0]
            direction = move[1]
            writer.writerow([n, game, algorithm, dimension, time, number_of_moves, number_of_states, won, state_space, car_key, direction])


def start_time():
    start = time.time()
    return start


def end_time(start):
    end = time.time()
    elapsed_time = round((end - start), 6)
    print(f"Puzzle was solved in {elapsed_time}s.")
    return elapsed_time


if __name__ == "__main__":
    game_name = "6x6_0"
    algorithm = "random"
    amount_of_times = "1"
    run_experiment(game_name, algorithm, amount_of_times)
