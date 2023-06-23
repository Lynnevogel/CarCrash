import os
from code.algorithms.random import Random
import time
    
def run_experiment(game_name, algorithm, amount_of_times):
    os.system("python3 main.py " + str(game_name) + " " + str(algorithm) + " " + amount_of_times)


def output(self, solution: list[list[str]]) -> None:
    """
    Writes a solution for a board into a csv file.
    """
    with open("output/output.csv", "w") as file:
        writer = csv.writer(file)
        field = ["car", "move"]

        writer.writerow(field)

        for move in solution:
            car_key = move[0]
            direction = move[1]
            writer.writerow([car_key, direction])

def start_time():
    start_time = time.time()
    return start_time

def end_time(start_time):
    end_time = time.time()
    elapsed_time = round((end_time - start_time), 4)
    print(f"Puzzle was solved in {elapsed_time}s.")
    
# if __name__ == "__main__":
#     game_name = "6x6_0"
#     algorithm = "random"
#     amount_of_times = "2"
#     run_experiment(game_name, algorithm, amount_of_times)
#     Algoritm = Random
#     for i in range(amount_of_times):
#         algorithm = Algoritm(board)
#         algorithm.go()  
#         i += 1
#         print(f"run: {i}")
#         print(f"aantal runs: {i}")